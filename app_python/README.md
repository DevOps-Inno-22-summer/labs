# Getting current time ![version-badge] [![CI Status](https://github.com/raghadsalameh1/labs/actions/workflows/python-app.yml/badge.svg?branch=lab3)](https://github.com/raghadsalameh1/labs/actions) ![Test workflow]

## Getting Started

1. Clone the repo to your device.
2. Change the directory to the app_python folder.
3. Create your virtual environment by running the command in cmd

    ```text
    py -3 -m venv .venv
    ```

4. Activate your environment by running the command in cmd

    ```text
    Set-ExecutionPolicy Unrestricted -Scope Process
    & "path/to/your/repo/app_python/.venv/Scripts/Activate.ps1"
    ```

5. Install all the required dependencies from **requirements.txt** file by running the command

    ```text
    pip install -r requirements.txt
    ```

6. To run the server, there are 2 ways:
   1. use the **.vscode** provided setting if you are using vscode IDE. or
   2. run the command

        ```text
        uvicorn src.main:app
        ```

7. To navigate to the project swagger document click on the link that uvicorn running on and add "/docs"

    ```text
    example: http://127.0.0.1:8000/docs
    ```  

8. To execute the written tests, first you need to install your application package by running the command:

    ```text
    pip install -e .
    ```

    then you can run tests. there are 2 ways:
    1. use the **.vscode** provided setting if you are using vscode IDE and run tests from testing tap. or
    2. run the command

        ```text
        pytest
        ```

9. For checking the code against security issues run the following command:

    ```text
    bandit -r src
    ```

10. For checking the maintainability of the code run the following command once:

    ```text
    wily build src/
    ```

    then run the following command each time you need a report:

    ```text
    wily report src
    ```

## About Dockerfile

- To build an image from the Dockerfile make sure that you create a build folder and add each of **src**,**tests**, **setup.py** to it.
- You can run a container from an image created from the docker files in 2 ways:
    1. Using .vscode attached setting. choose run Docker:Python - Fastapi
    2. Using cmd as the following

        ```text
        $docker build -t image_name .
        $docker run -d -p 8000:8000 --name container_name image_name
        ```

        to check the status of the running container if it is healthy or not by running the command

        ```text
         $docker inspect --format='' container_name
        ```

        or by seeing the status of the target container using:

        ```text
         $docker container ls
        ```

## About Continous Integration

For eash push or pull request on the bransh master and lab3 a pipeline with the following stages is run:
    - Installing requiered dependencies.
    - Lint with pylint
    - Test with pytest
    - Prepare build file for Dockerfile
    - Login to DockerHub
    - Build and push the Docker Image.

 [version-badge]: https://img.shields.io/badge/version-1.0-blue.svg
 [Test workflow]:https://img.shields.io/github/workflow/status/docker/build-push-action/test?label=test&logo=github&style=flat-square
