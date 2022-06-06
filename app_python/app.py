from datetime import datetime, timedelta, timezone
from flask import Flask

app = Flask(__name__)

moscow_time_zone = timezone(timedelta(hours=3))


def format_time(datetime_now):
    return datetime_now.strftime("%H:%M:%S")


def generate_moscow_time():
    return format_time(datetime.now(moscow_time_zone))


@app.route("/")
def index():
    return f"Moscow time is { generate_moscow_time() }"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
