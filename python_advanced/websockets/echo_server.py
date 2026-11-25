#!/usr/bin/env python3


"""Opens a websocket which will echo the received message"""


import asyncio
from websockets.asyncio.server import serve


async def echo(websocket):
    """waits for message to send back"""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """opens server on port"""
    server = await serve(echo, '127.0.0.1', 8765)
    await server.serve_forever()


asyncio.run(main())
