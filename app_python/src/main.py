from fastapi import FastAPI
from datetime import datetime
from pytz import timezone

app = FastAPI()


def getMoscowTime():
    mscw_time = datetime.now(timezone('Europe/Moscow'))
    return mscw_time.strftime('%Y-%m-%d_%H:%M:%S')


@app.get('/')
async def main():
    return({"Moscow time": getMoscowTime()})
