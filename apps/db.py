import traceback
import logging
import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import date, datetime
from decimal import Decimal
from sqlalchemy.orm.state import InstanceState
from apps.dbproperties import DBProp


prop = DBProp()

ECHO_LOG = False

engine = create_engine(
    prop.url,
    echo=ECHO_LOG,
    pool_size=prop.pool_size,
    max_overflow=prop.max_overflow,
    isolation_level=prop.isolation_level,
    )

Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def row_to_dict(rowobj):
    """
    SQLAlchemy Modelまたはクエリの実行結果の行オブジェクト(またはその配列)をdict(の配列)に変換
    """
    if '__dict__' in dir(rowobj):
        return rowobj.__dict__
    else:
        return dict(rowobj)


def to_dict(obj):
    """
    SQLAlchemyのormオブジェクトまたはsqlの実行結果（またはその配列）をdict（の配列）に変換
    """
    if isinstance(obj, list):
        for r in obj:
            return [row_to_dict(r) for r in obj]
    else:
        return row_to_dict(obj)


def json_converter(obj):
    """
    json変換のデフォルトを定義する。
    """
    if isinstance(obj, datetime):
        # 日時型は、文字列(isoformat(' '))に変換
        return obj.isoformat(' ', timespec='seconds')
    elif isinstance(obj, date):
        # 日付型は、文字列(isoformat)に変換
        # 【注意！】isinstanceは、datetime型なら、dateでもtrueになるので、
        # datetimeを先に判定してからdateを判定する。
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        # Decimal型は、floatに変換
        return float(obj)
    elif isinstance(obj, InstanceState):
        # SQLAlchemyのオブジェクトのInstanceStateプロパティは変換しない。
        return ''
    raise TypeError("Type %s not serializable" % type(obj))


def to_json(objects):
    '''
    dictオブジェクト（またはその配列）をjsonに変換する。
    '''
    objdict = to_dict(objects)
    return json.dumps(objdict, default=json_converter, ensure_ascii=False)
