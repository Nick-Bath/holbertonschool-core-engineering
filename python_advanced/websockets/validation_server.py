#!/usr/bin/env python3


"""Opens a websocket which will echo the received message"""


import asyncio
from websockets.asyncio.server import serve


async def echo(websocket):
    """waits for message to send back"""
    async for message in websocket:
        if isinstance(message, str):
            if len(message.strip()) == 0:
                await websocket.send("EER:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
        else:
            await websocket.send("Not a string")


async def main():
    """opens server on port"""
    server = await serve(echo, 'localhost', 8765)
    await server.serve_forever()


asyncio.run(main())
