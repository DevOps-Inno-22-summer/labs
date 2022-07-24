from flask import Flask
from datetime import datetime
import pytz
import logging


logging.basicConfig(filename='logs.txt',
                    encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)


@app.route('/')
def current_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    datetime_moscow = datetime.now(moscow_timezone)
    logging.debug('main function called :' + str(datetime_moscow))
    return f"Moscow: {datetime_moscow.strftime('%Y:%m:%d %H:%M:%S %Z %z')}"


@app.route('/visits')
def visits():
    logs = ''
    with open('logs.txt', 'r') as f:
        logs = f.read()
    return logs


if __name__ == '__main__':
    app.run()
