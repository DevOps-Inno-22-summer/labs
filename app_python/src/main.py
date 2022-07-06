"""System module"""
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from src.helpers.current_time import current_moscow_time, record_access, get_visits_content

app = FastAPI(title='DevOps Lap API')

@app.get("/", tags=["Current Time"])
async def moscow_time():
    """Current Moscow time"""
    record_access()
    moscow_time_now = current_moscow_time()
    return moscow_time_now

@app.get("/visits", tags=["Statistics"],response_class=PlainTextResponse)
async def visits():
    """get logs of the visits for the root pass"""
    contents = get_visits_content()
    return contents
    