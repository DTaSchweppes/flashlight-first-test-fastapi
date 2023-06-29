from enum import Enum

from fastapi import FastAPI, HTTPException

app = FastAPI()


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

@app.get("/light/{command}")
async def control_light(command: str, metadata: str = None):
    global LIGHT
    if command not in LIGHT.commands:
        raise HTTPException(status_code=400, detail="Unknown command.")
    method_name = LIGHT.commands[command]
    method = getattr(LIGHT, method_name)
    return method(metadata)
