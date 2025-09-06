import asyncio
import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        outgoing_message = "Привет, сервер!"
        print(f"Отправка: {outgoing_message}")
        await websocket.send(outgoing_message)

        for _ in range(5):
            message = await websocket.recv()
            print(f"Ответ от сервера: {message}")


asyncio.run(client())