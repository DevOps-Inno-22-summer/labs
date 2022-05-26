# DevOps Engineering Labs

The Innopolis University DevOps labs summer 2022 solutions
from Danila Goriachkin MSS-21.

## Authors

| Name              | E-mail            | Telegram | GitHub   |
| ----------------- | ----------------- | -------- | -------- |
| Danila Goryachkin | dndv279@gmail.com | @dndv279 | @DanilaG |

## Moscow time

The web application that shows Moscow time.

### Install

Install all dependency by the following command:

```
pip3 install -r app_python/requirements.txt
```

### Run

- Set `main.py` as a flask app file:

```
export FLASK_APP=app_python/main.py
```

- Set development mode in flask:

```
export FLASK_ENV=development
```

- Run flask:

```
flask run
```

- Open [`http://127.0.0.1:5000`](http://127.0.0.1:5000) at a browser.

### Testing

Run `time_provider_test.py` in the app_python for test execution:

```
cd app_python
python3 -m unittest time_provider_test.py
```

### Docker

The program image on docker hub [here](https://hub.docker.com/r/danilag/app-python).

#### Run docker

```
docker run -i -t -p 6123:5000 danilag/app-python
```

where 6123 is outside container port.

#### Build image

```
docker build --tag danilag/app-python ./app_python
```

### Static analyzes

#### .py files

We use `flake8`.

*Install:*

```
pip3 install flake8
```

*Run:*

```
flake8 app_python
```

#### .html files

We use `tidy-html5`.

*Install:*

```
brew install tidy-html5
```

*Run:*

```
tidy app_python/templates/index.html
```

#### .md files

We use `mdl`.

*Install:*

```
gem install mdl
```

*Run:*

```
mdl .
```

### Licence

We use [MIT License](app_python/LICENSE).
