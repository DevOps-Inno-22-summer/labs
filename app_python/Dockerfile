# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY build /app

# Creates a non-root user and adds permission to access the /app folder
RUN adduser --disabled-password appuser
USER appuser

CMD ["uvicorn","src.main:app", "--reload","--host","0.0.0.0"]