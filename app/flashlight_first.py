from fastapi import FastAPI, HTTPException
import asyncio
import json

app = FastAPI()

LIGHT_HOST = "127.0.0.1"  # IP фонаря
LIGHT_PORT = 9999  # порт фонаря


class FlashLight:
    colors = ['red', 'white', 'blue']
    commands = {
        'ON': 'turn_on',
        'OFF': 'turn_off',
        'COLOR': 'change_color',
    }

    def __init__(self):
        self.status = False  # По умолчанию выключен фонарь

    def turn_on(self, metadata: str = None):
        if self.status:
            return {"message": "Flashlight was already on"}
        self.status = True
        return {"message": "Flashlight turned on"}

    def turn_off(self, metadata: str = None):
        if not self.status:
            return {"message": "Flashlight was already off"}
        self.status = False
        return {"message": "Flashlight turned off"}

    def change_color(self, metadata: str):
        if metadata in self.colors:
            return {"message": f"Color is changed to {metadata}."}
        return {"message": f"Color not in list colors of flashlight."}



LIGHT = FlashLight()

async def send_command(command, metadata=None):
    """
    Функция для отправки команды на сервер фонаря
    :param command:
    :param metadata:
    :return:
    """
    data = {
        "command": command,
        "metadata": metadata
    }
    message = json.dumps(data)

    reader, writer = await asyncio.open_connection(LIGHT_HOST, LIGHT_PORT)
    writer.write(message.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()


@app.get("/light/{command}")
async def control_light(command: str, metadata: str = None):
    global LIGHT
    if command not in LIGHT.commands:
        raise HTTPException(status_code=400, detail="Unknown command.")
    method_name = LIGHT.commands[command]
    method = getattr(LIGHT, method_name)
    await send_command(method)
    return method(metadata)

