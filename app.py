from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    timez = timezone(timedelta(hours=3))
    date = datetime.now(timez)

    return render_template("home.html", result=date)

if __name__ == "__main__":
    app.run(debug=True)