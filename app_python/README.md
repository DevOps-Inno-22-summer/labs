## How the application works for lab 1:

- `Flask` is a small and lightweight Python web framework that provides useful tools and  features that make creating web applications in Python easier. It gives developers flexibility and is a more accessible framework for new developers since you can build a web application quickly using only a single Python file.
- The python time method `ctime()` converts a time expressed in seconds since the epoch to a string representing local time. If secs is not provided or None, the current time as returned by time() is used. This function is equivalent to asctime(localtime(secs)).
- The `ntplib` module offers a simple interface to query NTP servers from Python. 
- Consequently The method `print_time` prints the time that is in the machine where the app is running.
- `if __name__ == “main”:` is used to execute some code *only if the file was run directly*, and not imported. 

## Docker section (Lab2):

The Dockerfile creation of this work is based on the article [<em> How to Dockerize a Flask Application </em>](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)

- In this part of the project, a dockerfile is created. The `Dockerfile` starts with the installation of a python image (`FROM`), in which the application will run. This import is obvious since without python, the app would not run. 
- Next, I add the maintainer tag, in which I can let other users know who is the creator of this file. 
- There is a couple of `RUN` commands. The first RUN creates a directory in which all the application will be contained in the container, and the second RUN performs command line operations that are needed to run the application. 
- The `COPY` command works to copy the the files in our local working directory to the directory in the docker image.
- The `CMD` instruction contains a list of command line commands that will be executed when a container is created from the image. 
- Finally, there is an `EXPOSE` tag which simply lets Docker know that the container listens on the specified network ports at runtime. You can specify whether the port listens on TCP or UDP, and the default is TCP if the protocol is not specified. The EXPOSE instruction does not actually publish the port.

- The image can be downloaded from [my Docker Hub](https://hub.docker.com/r/robertrons/app_python/tags). To run the image, you must run this command: `docker run -p 5000:5000  robertrons/app_python:1.0` Then the app will run on: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Continuous integration (Lab3):

### Code testing:

The file *test_app.py* contains the tests for the *app.py* application file. To run the tests, please use the command `python -m unittest test_app` in a command line interface (cli). Check the file *PYTHON.md* for details of what the tests do.