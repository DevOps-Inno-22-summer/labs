'''Run web application'''

from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    '''Function'''
    time_zone = timezone(timedelta(hours=3))
    date = datetime.now(time_zone)

    with open("data/logs.txt", "a") as file:
        print(date, file=file)

    return render_template("home.html", result=date)


@app.route("/visits", methods=["GET"])
def visits():
    '''Function 2'''
    page = ""
    with open("data/logs.txt", "r", encoding="UTF-8") as file:
        for line in file:
            page += line + "<br>"
    return page


if __name__ == "__main__":
    app.run(debug=True)