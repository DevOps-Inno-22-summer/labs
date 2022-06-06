# DevOps Python Project

[![Python testing and Docker](https://github.com/ElBatanony/devops-labs/actions/workflows/python-ci.yml/badge.svg)](https://github.com/ElBatanony/devops-labs/actions/workflows/python-ci.yml)

This python project (so far) displays the current time in Moscow (timezone UTC +3).

The Python framework selected is [Flask](https://flask.palletsprojects.com/en/2.1.x/).

A test script is included to test generating the time and the HTML.

The linter used is [pylint](https://pylint.pycqa.org/en/latest/). The missing pydocs warning is turned off; due to adequate method names.

## Framework

Flask is used as it is a light-weight production-ready Python web framework.
Flask is popular with many examples and tutorials.
Given the known requirements of the course, Flask should be able to satisfy the needs of the labs.
Additionally, we discussed this choice in class and the professor approved of it.

## Serving the app

Run the following command in the command line

```console
python app.py
```

## Testing

The code for this project was written in a modular fashion to facilitate unit testing.

To run the tests, run the following command

```console
pytest app_test.py
```

The unit tests cover:

- Smoke test, i.e., time generation
- Time formatting
- HTML response

## Docker

Docker Hub [repository link](https://hub.docker.com/repository/docker/elbatanony/devops-python).

Building the image

```Docker
docker build -t elbatanony/devops-python:latest .
```

Running the container

```Docker
docker run -d -p 5000:5000 --name devops-python elbatanony/devops-python:latest
```
