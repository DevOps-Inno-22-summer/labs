from datetime import datetime
import pytz
import os
from flask import Flask
from moscow_logger import MoscowLogger as logger

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def moscow():
    logger.visitMainPage()
    tzone = 'Europe/Moscow'
    localDatetime = datetime.now().astimezone(pytz.timezone(tzone))
    return localDatetime.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/visits', methods=['POST', 'GET'])
def visitors():
    return logger.getVisitors().replace('\n', "<br>")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
