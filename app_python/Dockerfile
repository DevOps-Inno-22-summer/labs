FROM python:3.9.6-slim-buster

WORKDIR /home/app

RUN useradd -u 8877 ahmed

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000

COPY app.py app.py

USER ahmed

ENTRYPOINT ["python", "app.py"]
