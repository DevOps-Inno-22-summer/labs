from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def index():
    tz = pytz.timezone("Europe/Moscow")
    time = datetime.now(tz)
    return time.strftime("%H:%M:%S")
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    
    