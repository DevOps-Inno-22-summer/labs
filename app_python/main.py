"""System module"""
from fastapi import FastAPI
from app_python.helpers.current_time import current_moscow_time

app = FastAPI(title='DevOps Lap API')

@app.get("/", tags=["Current Time"])
async def moscow_time():
    """Current Moscow time"""
    moscow_time_now = current_moscow_time()
    return moscow_time_now
