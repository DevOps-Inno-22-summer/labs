# Use slim version of python package
FROM python:3.8-slim

# Expose port
EXPOSE 5000

# Set enviroment variables

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turn off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set Flask environment type
ENV FLASK_ENV=development

# Set Flask entrypoint
ENV FLASK_APP=main.py

# Set work directory, install pip requirements
WORKDIR /app_python
COPY . .
RUN python -m pip install -r requirements.txt

# Create a non-root user and adds permission to access the /app_python folder
RUN adduser --disabled-password appuser && chown -R appuser /app_python
USER appuser

# Create entrypoint
ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
