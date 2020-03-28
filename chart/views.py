import time
import json
from datetime import datetime as dt
from models import PriceData
from apps.app import api



# pricedata_instance
pricedata = PriceData(dbname="fxdata")
pricedata = pricedata.create_query()


@api.route('/ws', websocket=True)
async def websocket(ws):
    await ws.accept()
    try:
        while True:
            for row in pricedata:
                for x in row:
                    t = int(time.mktime(
                        dt.fromisoformat(
                            x['time'].strip("Z")).timetuple()))
                    close = float(x['Close'])
                    high = float(x['High'])
                    low = float(x['Low'])
                    Open = float(x['Open'])
                    data = [{"time": t, "y": close},
                            {"time": t, "y": high},
                            {"time": t, "y": low},
                            {"time": t, "y": Open}]
                    await ws.send_json(json.dumps(data))
    except Exception:
        await ws.close()
