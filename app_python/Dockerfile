# firstly, python image
FROM python:3.9-alpine

# create user instead of root
RUN adduser --home /app --shell /bin/sh --uid 1000 --disabled-password appuser
USER appuser

# expose port
EXPOSE 5000

# enviroment variables
ENV FLASK_ENV=development FLASK_APP=main.py

# switch working directory
WORKDIR /app

# copy files
COPY . .

# install the dependencies and packages from the requirements file
RUN pip3 install --no-cache-dir -r requirements.txt

# run app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
