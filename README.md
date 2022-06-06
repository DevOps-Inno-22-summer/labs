# CI

![example workflow](https://github.com/AsWeSee/devopslabs_summer22/actions/workflows/github-actions-tests.yml/badge.svg)


# README

## Install (Windows)
```
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```
## Local run
```
python .\app_python\app.py
```
or
```
cd .\app_python\
flask run
```
## !!! Important for production !!!

Build-in Flask server not ready for production. To use in prod cover flask with WSGI or something like nginx

## Pylint
To use pylint run
```
pylint app.py
```


## Tests
'''
pytest .\app_python\tests.py
'''