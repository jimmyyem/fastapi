import asyncio
import websockets
import time
import json

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Send messages periodically
        async def send_messages():
            i = 1
            while True:
                message = f"Hello from Python client {i}"
                await websocket.send(json.dumps({
                    "message": message,
                    "msgType": "FriendTalkNotice"
                }))
                print(f"Sent: {message}")
                i += 1
                await asyncio.sleep(2)

        # Receive messages
        async def receive_messages():
            async for message in websocket:
                print(f"Received: {message}")

        # Run sender and receiver concurrently
        await asyncio.gather(send_messages(), receive_messages())

if __name__ == "__main__":
    asyncio.run(client())