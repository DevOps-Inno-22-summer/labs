"""Flask web application to show current Moscow time."""
from datetime import datetime
from flask import Flask, render_template
import pytz

app = Flask(__name__)


def current_moscow_time():
    """Get current Moscow time."""
    return datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")

def log_to_file(time):
    """Wite logs to file."""
    with open('data/visits.txt', 'a') as f:
        print(time, file=f)

def log_from_file():
    """Read logs from file."""
    with open('data/visits.txt') as f:
        logs = f.readlines()
    return '<br>'.join(logs)

@app.route('/')
def main():
    """Generate main html page."""
    cur_time = current_moscow_time()
    log_to_file(cur_time)
    return render_template('time.html', moscow_time=cur_time)

@app.route('/visits', methods=['GET'])
def visitors():
    """Get visitors."""
    return log_from_file()

if __name__ == '__main__':
    app.run()
