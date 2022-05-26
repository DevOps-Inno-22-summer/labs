from flask import Flask, render_template
from time_provider import TimeProvider

app = Flask(__name__)


@app.route('/')
def index():
    time = TimeProvider().msk()
    return render_template('index.html', time=time)
