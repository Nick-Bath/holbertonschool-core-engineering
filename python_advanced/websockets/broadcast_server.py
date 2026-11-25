#!/usr/bin/env python3

"""Opens a unicast server and responds to multiple clients
    at once via broadcast
"""


import asyncio
from websockets.asyncio.server import serve, broadcast
import websockets


CONNECTED_CLIENTS = set()


async def handler(websocket):
    """tracks connections, echos messages received to all connections"""
    CONNECTED_CLIENTS.add(websocket)
    # print(f"Client connected: {websocket.remote_address} | "
    # f"TC: {len(CONNECTED_CLIENTS)}")

    try:
        # listen for messages
        async for message in websocket:
            broadcast(CONNECTED_CLIENTS, f"B:{message}")
    except websockets.exceptions.ConnectionClosed:
        # raised when client disconnects
        pass
    finally:
        # disconnection detected
        CONNECTED_CLIENTS.remove(websocket)
        # print(f"{websocket.remote_address} disconnected |"
        # f"TC: {len(CONNECTED_CLIENTS)}")


async def main():
    """opens server"""
    async with serve(handler, '127.0.0.1', 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
