# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app_python

COPY app_python/app.py .
COPY app_python/LocalLogger.py .
# COPY --chown=app:app app-files/ /app
RUN adduser -u 3232 --disabled-password appuser && chown -R appuser /app_python/app.py
USER appuser

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]