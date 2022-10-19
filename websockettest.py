from email import header
from typing import final
import requests
import os
from dotenv import load_dotenv
import http.client
import json
import time
import threading
from datetime import datetime
import asyncio
import websockets
from zoneinfo import ZoneInfo


conn3 = http.client.HTTPSConnection("reiseauskunft.bahn.de")


# Load api via dotenv #
load_dotenv()
AeroAPIkey = os.getenv('AeroAPIkey')
clientId = os.getenv('clientId')
clientSecret = os.getenv('clientSecret')

headers = {
    'x-apikey': AeroAPIkey,
    'DB-Client-Id': clientId,
    'DB-Api-Key': clientSecret,
    'accept': "application/xml",
    'accept': "application/json",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }


def requestloop():
    while True:
        now = datetime.now(ZoneInfo('Europe/Berlin'))
        current_time = now.strftime("%H:%M:%S")
        conn3.request("GET", f"/bin/bhftafel.exe/dn?L=vs_java&start=yes&boardType=arr&time={current_time}&input=8011160")
        res = conn3.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        list = data.split("\n")
        list = [ x for x in list if "+" in x ]
        list2 = ' '.join(list)
        list = list2.split("+ ")
        finallist = str(len(list))
        time.sleep(5)
        async def hello():
            async with websockets.connect("ws://localhost:3000") as ws:
                await ws.send(finallist)
                await ws.recv()
        #print(finallist)
        #print("\r", end="", flush=True),

        asyncio.run(hello())

requestloop()