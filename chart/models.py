import sys
import pathlib

from influxdb import InfluxDBClient

"""上の階層のファイルを読み込むための処理
"""
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')


class PriceData():
    """
    クライアントを作成し、クエリを実行する。
    小河原さんのcsvデータをそのまま流用して試作したので、
    oanda取得データに直す必要あります。
    テーブル定義：
    　　テーブル名:value
        time:時間
        Close:終値
        High:高値
        Low:安値
        Open:始値
        Volume:取引高
        host:←これはいらないですね。
    """
    def __init__(self,
                 host='localhost',
                 port=8086,
                 user='root',
                 password='root',
                 dbname=''):
        """
        args:
            host:influxdbのホスト名
            port:influxdbのあるポート名
            user:ユーザー名
            password:パスワード
            dbname:データベース名
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname

    def instance_client(self):
        """influxdbのクライアント作成
        """
        client = InfluxDBClient(
            self.host,
            self.port,
            self.user,
            self.password,
            self.dbname)
        return client

    def create_query(self):
        """クエリを実行する
        """
        query = 'select * from /.*/ '
        result = self.instance_client().query(query)
        self.instance_client().close()
        return result
