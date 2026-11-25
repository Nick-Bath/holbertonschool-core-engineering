#!/usr/bin/env python3


"""client server connecting to websocket, sending and receiving messages"""


from websockets.asyncio.client import connect
import asyncio


async def hello():
    """connects to server, sends a msg and prints the response"""
    async with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello WebSocket")
        message = await websocket.recv()
        print(message)


if __name__ == "__main__":
    asyncio.run(hello())
