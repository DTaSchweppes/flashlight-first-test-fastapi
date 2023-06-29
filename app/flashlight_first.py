from enum import Enum

from fastapi import FastAPI, HTTPException
import asyncio
import json

app = FastAPI()

LIGHT_HOST = "127.0.0.1"  # IP фонаря
LIGHT_PORT = 9999  # порт фонаря


class CommandsLight(Enum): #перечисление команд
    ON = 'turn_on'
    OFF = 'turn_off'
    COLOR = 'change_color'


class ColorsLight(Enum): #перечисление цветов
    red = 'red'
    white = 'white'
    blue = 'blue'
    green = 'green'


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
async def control_light(command: str, metadata: float = None):
    if command == CommandsLight.ON.value:
        await send_command("ON")  # Включение фонаря
        return {"message": "Flashlight is turned on."}
    elif command == CommandsLight.OFF.value:
        await send_command("OFF")  # Выключение фонаря
        return {"message": "Flashlight is turned off."}
    elif command == CommandsLight.COLOR.value and metadata in ColorsLight:
        await send_command("COLOR", metadata)  # Смена цвета фонаря
        return {"message": f"Color is changed to {metadata}."}
    else:
        raise HTTPException(status_code=400, detail="Unknown command.")
