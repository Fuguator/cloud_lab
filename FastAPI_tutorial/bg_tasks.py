from fastapi import FastAPI, BackgroundTasks
import time
import asyncio

app = FastAPI()


def sync_task():
    time.sleep(3)
    print("email sending")


async def async_task():
    await asyncio.sleep(3)
    print("API request")

@app.post("/")
async def some_route(bg: BackgroundTasks):
    ...
    # asyncio.create_task(async_task())
    bg.add_task(sync_task)
    return {"success": True}