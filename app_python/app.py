from datetime import datetime, timedelta, timezone
from flask import Flask

app = Flask(__name__)


def generate_moscow_time():
    moscow_time_zone = timezone(timedelta(hours=3))
    time = datetime.now(moscow_time_zone).strftime("%H:%M:%S")
    return time


@app.route("/")
def index():
    return f"Moscow time is { generate_moscow_time() }"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
