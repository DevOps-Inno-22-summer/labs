![Build](https://github.com/war-and-peace/devops_labs/actions/workflows/python-app.yml/badge.svg)

## Web application

Flask is a production ready web framework that is used in many industrial projects successfully.
It is a very simple framework and best suited to small projects. It's also relatively fast both in terms of execution and development time.

## Run on local machine
Go to the app_python folder and run `python -m flask run` which runs the applications.
You can then go to `http://127.0.0.1:5000` to see the web application browser.


## Build Docker image
In order to build the docker image locally run the following:
```
    docker build app_python/ -t app_python_image
```
and run using:
```
    docker run app_python_image
```

## Run from docker hub
The public repository is available in docker hub. You can pull the repository and run it in the following way. TO pull the docker image run:
```
    docker pull megara/devops-app-python
```

In order to run the container execute the following command:

```
    docker run megara/devops-app-python
```

The logs show at what address the app is running inside the container (with a link to it). You can follow that link on browser and see the result.

## Unit tests
The application contains unit tests and its integrated into GitHub actions. The pipeline is successful when the application builds and all the tests pass.
