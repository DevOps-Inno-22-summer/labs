from fastapi import FastAPI
from datetime import datetime
from pytz import timezone

app = FastAPI()


@app.get('/')
def main():
    mscw_time = datetime.now(timezone('Europe/Moscow'))
    return({"Moscow time": mscw_time.strftime('%Y-%m-%d_%H:%M:%S')})
