# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim
LABEL maintainer=“a.vinov@innopolis.university”

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# This is the command that runs the application in the container
ENTRYPOINT [ "python3" ]

# This appends the list of parameters to the EntryPoint parameter to perform the command that runs the application. 
CMD [ "moscow_time.py" ]
