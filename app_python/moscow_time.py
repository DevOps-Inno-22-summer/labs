from datetime import datetime
import pytz
import os
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def moscow():
    tzone = 'Europe/Moscow'
    localDatetime = datetime.now().astimezone(pytz.timezone(tzone))
    return localDatetime.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
