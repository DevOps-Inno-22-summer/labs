# Description:

This is a simple fastapi application which shows Moscow time and date.

# Dependencies:

For installing dependencies, run the following command in the terminal:

    cd app_python

    pip install -r requirements.txt

# Running the application:

For running the application:

    cd app_python

    uvicorn main:app --reload

# Docker image:

For building docker image from repo:

    docker build --tag time-python .

For Running:

     docker run  -p 5000:5000 time-python

Repo is also deployed to docker hub so that it can be accessed from anywhere.
For pulling the image from docker hub:

    docker pull raminafandi/time-python:time-python

For running the image:

    docker run raminafandi/time-python:time-python

# Testing:

For testing the application:

    cd app_python
    pytest
