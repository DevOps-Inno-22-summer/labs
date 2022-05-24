from datetime import datetime
import pytz
from flask import Flask

app = Flask(__name__)


@app.route('/')
def moscow():
    utcmoment_naive = datetime.utcnow()
    utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)

    localFormat = "%Y-%m-%d %H:%M:%S"

    tzone = 'Europe/Moscow'
    localDatetime = utcmoment.astimezone(pytz.timezone(tzone))
    return localDatetime.strftime(localFormat)