from fastapi import FastAPI
import asyncio
from core.amara_core import start_amara
from guard.guard_ai import guard_check

app = FastAPI()

@app.on_event("startup")
async def startup():
    if guard_check():
        asyncio.create_task(asyncio.to_thread(start_amara))

@app.get("/")
def root():
    return {"status": "Amara CORE beží – autonómne generuje výstupy"}