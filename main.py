import subprocess
import asyncio
from app.flashlight_first import app
import uvicorn
requirements_file = 'requirements.txt' # путь к файлу requirements.txt
subprocess.check_call(['pip', 'install', '-r', requirements_file])  # Вызов pip для установки зависимостей

if __name__ == "__main__":
    asyncio.run(uvicorn.run(app))