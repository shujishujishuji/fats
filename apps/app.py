import sys
import logging
from logging import config, getLogger
import yaml
import responder
from pathlib import Path

"""上の階層のファイルを読み込むための処理
"""
current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')


def create_app():
    # static dir
    ROOT_DIR = Path(__file__).resolve().parents[2]

    # logging setup
    config.dictConfig(yaml.safe_load(open('settings/logging.conf').read()))
    logger = getLogger("fats")

    # declare responder
    api = responder.API(static_dir=str(ROOT_DIR.joinpath('static')),
                        )

    return api


api = create_app()
