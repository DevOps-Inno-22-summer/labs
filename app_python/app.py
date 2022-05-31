from flask import Flask, render_template
import os
from local_time import get_current_time

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    time = get_current_time(3)
    return render_template("index.html", result=time)


if __name__ == "__main__":
    app.run()
