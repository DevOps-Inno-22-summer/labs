from flask import Flask, render_template
from time_provider import TimeProvider
from visits_logger import VisitsLogger

app = Flask(__name__)


@app.route('/')
def index():
    time = TimeProvider().msk()
    VisitsLogger.main_page()
    return render_template('index.html', time=time)


@app.route('/visits')
def visits():
    return VisitsLogger.get_visitors().replace('\n', '<br>')
