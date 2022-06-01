# DevOps Python Project

This python project (so far) displays the current time in Moscow (timezone UTC +3).

The Python framework selected is [Flask](https://flask.palletsprojects.com/en/2.1.x/).

A test script is included to test generating the time and the HTML.

The linter used is [pylint](https://pylint.pycqa.org/en/latest/). The missing pydocs warning is turned off; due to adequate method names.

## Framework

Flask is used as it is a light-weight production-ready Python web framework.
Flask is popular with many examples and tutorials.
Given the known requirements of the course, Flask should be able to satisfy the needs of the labs.
Additionally, we discussed this choice in class and the professor approved of it.

## Serving the app

Run the following command in the command line

```console
python app.py
```

## Testing

To run the tests, run the following command

```console
python app_test.py
```

The tests include:

- Testing the time format
- Testing the HTML response
