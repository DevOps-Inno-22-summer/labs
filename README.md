# Labs

## Description

The first lab is about to develop and test a simple Python web application, that shows current time in Moscow.

`moscow_time.py` - flask web script
`moscow_time_test.py` - tests

## How to install

#### Install dependencies
```python
pip3 install pytz
pip3 install flask
```

#### Start web server
```bash
export FLASK_APP=moscow_time
export FLASK_ENV=development
flask run
```

#### Guides that used to build the app
1. [First](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-ru)
2. [Second](https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html)
3. [Third](https://flask-russian-docs.readthedocs.io/ru/latest/installation.html#installation)


#### Docker

Create image
`docker image build -t <container-name> .`

Run container for test
`docker run --publish 5000:5000 <container-name>`

Publish container to the DockerHub
`docker push <container-name>`


## Testing

#### Best practices

- Plan software Tests
- Use development practices that are Test-Oriented (TDD, patterns)
- Ensure all Tests are integrated in CI/CD pipeline
- Use proper type of testing (White-Black box, mutation, random, etc.)
- Develop requirements that are Testable

#### Run tests

```bash
python3 -m unittest moscow_time_test
```