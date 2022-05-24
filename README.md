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

### Recommended workflow

#### For the first lab
1. Fork this repository on your workspace
2. Checkout master branch
3. Complete lab1 tasks
4. Push the code to your repository
5. Create PR to lab1 branch on this repository
6. Wait for your grade

#### For all other labs
1. Checkout the commit where you finished the previous lab
2. Complete tasks of current lab
3. Push the code to your repository
4. Create PR to labN branch on this repository
5. Wait for your grade