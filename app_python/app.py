import os
import json

from datetime import datetime, timedelta, timezone

from flask import Flask, jsonify


app = Flask(__name__)

moscow_time_zone = timezone(timedelta(hours=3))

VISITS_FILE = "/home/app/data/visits.json"


def format_time(datetime_now):
    return datetime_now.strftime("%H:%M:%S")


def generate_moscow_time():
    return format_time(datetime.now(moscow_time_zone))


def read_visist():
    visits = 0
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "r", encoding="UTF-8") as file:
            visits = json.load(file)
    return jsonify(visits)


def write_visits(visits):
    with open(VISITS_FILE, "w", encoding="UTF-8") as file:
        json.dump(visits + 1, file)


def create_visits_file():
    os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)


def log_visit():
    visits = 0
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "r", encoding="UTF-8") as file:
            visits = json.load(file)
    else:
        create_visits_file()
    write_visits(visits)


@app.route("/")
def index():
    log_visit()
    return f"Moscow time is { generate_moscow_time() }"


@app.route("/visits")
def visit():
    return read_visist()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
