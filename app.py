'''Run web application'''

from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    '''Function'''
    time_zone = timezone(timedelta(hours=3))
    date = datetime.now(time_zone)

    return render_template("home.html", result=date)

if __name__ == "__main__":
    app.run(debug=True)