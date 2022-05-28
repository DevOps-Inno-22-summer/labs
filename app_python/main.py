from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def main():
    cur_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")
    return render_template('time.html', moscow_time=cur_time)

if __name__ == '__main__':
    app.run()
