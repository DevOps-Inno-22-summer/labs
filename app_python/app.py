'''Run web application'''

from flask import Flask, render_template, request
from local_time import get_current_time

LOGS_FILENAME = "logs/visits.log"

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    '''Main page of web application'''
    time = get_current_time(3)
    with open(LOGS_FILENAME, "a", encoding="UTF-8") as file:
        addr = str(request.remote_addr)
        file.write(addr + " : " + time + "\n")
    return render_template("index.html", result=time)


@app.route("/visits", methods=["GET"])
def visits():
    '''Page which show the content of file with visited users'''
    result = ""
    with open(LOGS_FILENAME, "r", encoding="UTF-8") as file:
        for line in file:
            result += line + "<br />"
    return result


if __name__ == "__main__":
    app.run()
