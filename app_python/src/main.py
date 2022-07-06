from fastapi import FastAPI
from datetime import datetime
from pytz import timezone
import logging
app = FastAPI()

# create log file
logging.basicConfig(filename='logs.log',
                    encoding='utf-8', level=logging.DEBUG)


def getMoscowTime():
    mscw_time = datetime.now(timezone('Europe/Moscow'))
    return mscw_time.strftime('%Y-%m-%d_%H:%M:%S')


@app.get('/')
async def main():
    logging.debug('main function called :' + getMoscowTime())
    return({"Moscow time": getMoscowTime()})


@app.get('/visits')
async def visits():
    # get logs from logs.log file
    with open('logs.log', 'r') as f:
        logs = f.read()
    return logs
