"""Importing required libraries"""

import datetime
from flask import Flask, render_template
import pytz


app = Flask(__name__)

#Generate Moscow according to current timezone.
def moscow_time_now():
    """Get moscow time zone"""

    moscow_time = pytz.timezone("Europe/Moscow")

    current_time=datetime.datetime.now(moscow_time)

    return current_time.strftime('%H:%M:%S')

#Call the time function.
@app.route("/")
def index():
    """ Returns the current time in MOSCOW """
    return render_template("index.html",content= moscow_time_now())
if __name__ == "__main__":
    app.run(debug=True)
