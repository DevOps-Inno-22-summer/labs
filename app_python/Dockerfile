# syntax=docker/dockerfile:1

# Not using slim version of image because of issue in django dependency
# https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app_python

COPY requirements.txt requirements.txt
COPY . .

RUN pip install -r requirements.txt

RUN addgroup --system app && adduser --system --group app
USER app

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
