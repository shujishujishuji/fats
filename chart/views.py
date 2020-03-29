import time
import json
from datetime import datetime as dt
from chart.models import PriceData
from chart.service import make_generater, streamer
from apps.app import api


# pricedata_instance
pricedata = PriceData(dbname="fxdata")
pricedata = pricedata.create_query()


async def websocket(ws):
    await ws.accept()
    try:
        ticks = make_generater(pricedata)
        for x in streamer(ticks):
            await ws.send_json(json.dumps(x))
    except Exception:
        await ws.close()
