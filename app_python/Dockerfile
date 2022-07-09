# syntax=docker/dockerfile:1
FROM python:3.11.0b3-bullseye

LABEL maintainer="r.chavez@innopolis.ru"

RUN mkdir -p /app_python  

WORKDIR /app_python

RUN pip3 install --upgrade pip &&\
    pip3 install flask &&\
    pip install ntplib

COPY . .

ENV FLASK_APP=app.py

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000

