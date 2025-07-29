import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f"Received: {message}")
        response = f"Server echo: {message}"
        await websocket.send(response)
        print(f"Sent: {response}")

async def main():
    wshost = "localhost"
    wsport = 8765
    server = await websockets.serve(echo, wshost, wsport)
    print(f"WebSocket server started at ws://{wshost}:{wsport}")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())