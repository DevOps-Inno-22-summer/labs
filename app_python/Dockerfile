FROM python:3.9-alpine

RUN apk add --no-cache curl

# Copy python requirements file
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Add our application files
RUN mkdir app
COPY ./app /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8080

CMD ["python3", "-m", "app"]
HEALTHCHECK CMD curl --fail http://localhost:8080/api/v1/health || exit 1
