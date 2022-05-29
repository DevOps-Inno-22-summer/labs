# Getting current time ![version-badge]

## Getting Started

1. Clone the repo to your device.
2. Change the directory to the lab folder.
3. Create your virtual environment by running the command in cmd

    ```text
    py -3 -m venv .venv
    ```

4. Activate your environment by running the command in cmd

    ```text
    Set-ExecutionPolicy Unrestricted -Scope Process
    & "path/to/your/repo/labs/.venv/Scripts/Activate.ps1"
    ```

5. Install all the required dependencies from **requirements.txt** file by running the command

    ```text
    pip install -r requirements.txt
    ```

6. To run the server, there are 2 ways:
   1. use the **.vscode** provided setting if you are using vscode IDE. or
   2. run the command

        ```text
        uvicorn app_python.main:app
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
    bandit -r app_python
    ```

10. For checking the maintainability of the code run the following command once:

    ```text
    wily build app_python/
    ```

    then run the following command each time you need a report:

    ```text
    wily report app_python
    ```

 [version-badge]: https://img.shields.io/badge/version-1.0-blue.svg
