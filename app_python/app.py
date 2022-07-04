from flask import Flask
from datetime import datetime
import pytz
from flask_healthz import healthz
from locallogger import LocalLogger as locallogger

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    locallogger.addVisit()
    tz = pytz.timezone("Europe/Moscow")
    time = datetime.now(tz)
    return time.strftime("%H:%M:%S")

def create_app():
    app.run(host="127.0.0.1", port=5000, debug=True)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    
@app.route('/visits', methods=['GET'])
def visitors():
    return locallogger.getVisits().replace('\n', "<br>") #<br> template hack