# DevOps course at Innopolis University

## Task

Python web application, that shows current time in Moscow.

## Getting Started

1. Need to be installed: Python 3.9+, pip.

2. Clone repository and go to folder with app.

```sh
git clone git@github.com:NastyRu/DevOps_labs.git
cd DevOps_labs/app_python
```

3. Create virtual environment and install packages.

```sh
python3 -m venv env
. ./env/bin/activate
pip install -r requirements.txt
```

4. Now you can run the application and tests.

```sh
python main.py
pytest test.py
```

4. Dockerfile.

You can find image [here](https://hub.docker.com/repository/docker/nastyru/flask-app-current-time).

And to run app.
```sh
docker image build -t flask_docker .
docker run -p 5001:5000 -d flask_docker
```
