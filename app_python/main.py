"""Flask web application to show current Moscow time."""
from datetime import datetime
from flask import Flask, render_template
import pytz

app = Flask(__name__)


def current_moscow_time():
    """Get current Moscow time."""
    return datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")


@app.route('/')
def main():
    """Generate main html page."""
    cur_time = current_moscow_time()
    return render_template('time.html', moscow_time=cur_time)

if __name__ == '__main__':
    app.run()
