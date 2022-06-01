from flask import Flask
import ntplib
from time import ctime

app = Flask(__name__)

@app.route("/")
def print_time():
    ntpClient = ntplib.NTPClient()
    response = ntpClient.request('pool.ntp.org')
    return ctime(response.tx_time)

if __name__ == '__main__':
    app.run()