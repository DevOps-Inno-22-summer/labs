
# README

## Install (Windows)
```
python -m venv env
.\venv\Scripts\activate
pip install -r requirements.txt
```
## Local run
```
python app.py
```
or
```
flask run
```
## Docker build and run
```
docker image build -t devopslab .
docker run -p 5001:5000 -d devopslab
```

## !!! Important for production !!!

Build-in Flask server not ready for production. To use in prod cover flask with WSGI or something like nginx

## Pylint
To use pylint run
```
pylint app.py
```
