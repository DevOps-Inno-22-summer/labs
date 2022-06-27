FROM python:3.9.6-slim-buster

WORKDIR /home/app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000

COPY app.py app.py

ENTRYPOINT ["python", "app.py"]
