from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def current_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    datetime_moscow = datetime.now(moscow_timezone)
    return f"Moscow: {datetime_moscow.strftime('%Y:%m:%d %H:%M:%S %Z %z')}"


if __name__ == '__main__':
    app.run()
