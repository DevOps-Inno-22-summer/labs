FROM python:3.9-slim

#copying the app to the container
COPY ./src /app_python/src
COPY ./requirements.txt /app_python

#setting up the working directory
WORKDIR /app_python

#installing the requirements
RUN pip3 install -r requirements.txt

EXPOSE 5000

#run the app with non-root user
RUN chown -R 1000:1000 /app_python

#command to run the app
CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--port=5000", "--reload"]