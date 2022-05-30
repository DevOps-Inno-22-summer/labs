from flask import Flask, render_template
from get_time import GetTime

app = Flask(__name__)

@app.route("/")
def index():
    msk_time = GetTime.get_moscow_time()
    msk_time_api = GetTime.get_moscow_time_api()
    return render_template('index.html', msk_time = msk_time, msk_time_api = msk_time_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
