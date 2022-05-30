# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

RUN useradd -ms /bin/bash newuser

USER newuser
# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . /home/newuser/code
WORKDIR /home/newuser/code

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "app_python/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
