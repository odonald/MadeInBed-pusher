from email import header
<<<<<<< HEAD
=======
from typing import final
>>>>>>> 1062f7d (Took two weeks to search, discover and figure multiple solutions for a good any relieable way, to push live data to a front end without having to refresh the browser. in the end I'm using Websockets, was pretty intense getting this to work.)
import requests
import os
from dotenv import load_dotenv
import http.client
import json
import time
import threading
from datetime import datetime
<<<<<<< HEAD
=======
import asyncio
import websockets

>>>>>>> 1062f7d (Took two weeks to search, discover and figure multiple solutions for a good any relieable way, to push live data to a front end without having to refresh the browser. in the end I'm using Websockets, was pretty intense getting this to work.)


conn1 = http.client.HTTPSConnection("apis.deutschebahn.com")
conn3 = http.client.HTTPSConnection("reiseauskunft.bahn.de")
#conn2 = http.client.HTTPSConnection("aeroapi.flightaware.com")


# Load api via dotenv #
load_dotenv()
AeroAPIkey = os.getenv('AeroAPIkey')
clientId = os.getenv('clientId')
clientSecret = os.getenv('clientSecret')

# Set headers for apicall including AeroAPI key #
# headers = {'x-apikey': AeroAPIkey, 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# Make call to AeroApi {500 free requests/Month} requesting delay data of specific airport via ID #
# delay_flights = requests.get(f'https://aeroapi.flightaware.com/aeroapi/airports/KIAH/delays', headers=headers)

# Check API response, save data to dataset_flight and print values #
# if delay_flights.status_code == 200:
#        dataset_flight = delay.json()
#        print(dataset_flight)

#db headers#
headers = {
    'x-apikey': AeroAPIkey,
    'DB-Client-Id': clientId,
    'DB-Api-Key': clientSecret,
    'accept': "application/xml",
    'accept': "application/json",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }


#conn1.request("GET", "/db-api-marketplace/apis/fahrplan/v1/journeyDetails/829134", headers=headers)
#res = conn1.getresponse()
#data = res.read()

#print(data.decode("utf-8"))

#conn2.request("GET", "/aeroapi/airports/KIAH/delays", headers=headers)

#res2 = conn2.getresponse()
#data2 = res2.read()

#print(data2.decode("utf-8"))

<<<<<<< HEAD

=======
>>>>>>> 1062f7d (Took two weeks to search, discover and figure multiple solutions for a good any relieable way, to push live data to a front end without having to refresh the browser. in the end I'm using Websockets, was pretty intense getting this to work.)
def requestloop():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        conn3.request("GET", f"/bin/bhftafel.exe/dn?L=vs_java&start=yes&boardType=arr&time={current_time}&input=8096003", headers=headers)
        res = conn3.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        list = data.split("\n")
        list = [ x for x in list if "+" in x ]
        list2 = ' '.join(list)
        list = list2.split("+ ")
<<<<<<< HEAD
        time.sleep(5)
        print(len(list), end="", flush=True)
        print("\r", end="", flush=True),

requestloop()

#thread1 = threading.Thread(target=timeloop)
#thread1.start()

#thread2 = threading.Thread(target=requestloop)
=======
        print(list)
        finallist = len(list)
        time.sleep(5)
        print(finallist)
        print("\r", end="", flush=True),
        async def hello():
            async with websockets.connect("ws://localhost:5000") as websocket:
                await websocket.send(str(finallist))
                await websocket.recv()

        asyncio.run(hello())

def requestloop2():
    while True:
        conn1.request("GET", "/db-api-marketplace/apis/fahrplan/v1/location/Frankfurt", headers=headers)
        res1 = conn1.getresponse()
        data1 = res1.read()
        time.sleep(7)
        print(data1.decode("utf-8"), end="",)
        


thread1 = threading.Thread(target=requestloop)
thread1.start()

#thread2 = threading.Thread(target=requestloop2)
>>>>>>> 1062f7d (Took two weeks to search, discover and figure multiple solutions for a good any relieable way, to push live data to a front end without having to refresh the browser. in the end I'm using Websockets, was pretty intense getting this to work.)
#thread2.start()    