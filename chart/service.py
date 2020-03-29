import time
import json
from datetime import datetime as dt


def make_generater(data):
    """
    ジェネレータの生成
    args: pricedata
    """
    ticks = (tick for price_list in data for tick in price_list)
    return ticks


def tick_parser(tick):
    """
    ティックデータの整形
    args:tickdata
    """
    t = int(time.mktime(
                dt.fromisoformat(
                    tick['time'].strip("Z")).timetuple()))
    close = float(tick['Close'])
    high = float(tick['High'])
    low = float(tick['Low'])
    Open = float(tick['Open'])
    data = [{"time": t, "y": close},
            {"time": t, "y": high},
            {"time": t, "y": low},
            {"time": t, "y": Open}]
    return data


def streamer(ticks, sleep_time=1):
    """
    ジェネレータをストリーミング出力する。
    args: ticks
    """
    for tick in ticks:
        tick_data = tick_parser(tick)
        # print(tick_data)
        yield(tick_data)

