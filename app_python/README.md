# DevOps Python Project

This python project (so far) displays the current time in Moscow (timezone UTC +3).

The Python framework selected is [Flask](https://flask.palletsprojects.com/en/2.1.x/).

A test script is included to test generating the time and the HTML.

The linter used is [pylint](https://pylint.pycqa.org/en/latest/). The missing pydocs warning is turned off; due to adequate method names.

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
