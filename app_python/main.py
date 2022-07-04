from flask import Flask, render_template
from get_time import GetTime
from logger import Logger

app = Flask(__name__)

@app.route("/")
def index():
    msk_time = GetTime.get_moscow_time()
    msk_time_api = GetTime.get_moscow_time_api()
    Logger.log_visit()
    return render_template('index.html', msk_time = msk_time, msk_time_api = msk_time_api)

@app.route("/visits")
def visits():
    Logger.log_visit('/visits')
    return render_template('visits.html', visits = Logger.get_visits())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
