# syntax=docker/dockerfile:1

# Base image (official)
FROM python:3.8-slim-buster

# Meta information
LABEL author.name="Danila Goryachkin"

# Expose port
EXPOSE 5000

# Set enviroment variables
ENV FLASK_ENV=development FLASK_APP=main.py

# Set work directory
WORKDIR /app_python

# Create a not-root user
RUN adduser --disabled-password appuser && chown -R appuser /app_python
USER appuser

# Copy files
COPY . .

# Instal requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# Run application in
ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
