"""Flask web application to show current Moscow time."""
from datetime import datetime
from flask import Flask, render_template
import pytz

app = Flask(__name__)

@app.route('/')
def main():
    """Generate main html page."""
    cur_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")
    return render_template('time.html', moscow_time=cur_time)

if __name__ == '__main__':
    app.run()
