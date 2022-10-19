import asyncio
import websockets

while True:
    yourmessage = input(str("type your message: "))

    async def hello():
        async with websockets.connect("ws://localhost:3000") as websocket:
            await websocket.send(yourmessage)
            await websocket.recv()

    asyncio.run(hello())