# DevOps Engineering labs

Alexander Stepanov M21-SE-01

## Moscow local time

The web application that shows Moscow local time.

### Run

```sh
# Go to the app folder
cd app_python

# Create virtual environment
python3 -m venv env

# Open virtual environment
. ./env/bin/activate

# Upgrade pip
pip install -U pip

# Install requirements
pip install -r requirements.txt

# Run the app
python -m flask run
```

### Docker

You can find the image [here](https://hub.docker.com/repository/docker/willsem/moscow-local-time).

#### Makefile commands

All commands should be run at `app_python` directory

##### Build image localy

```sh
make build
```

##### Run image localy

```sh
make run
```

After the run, application would be able at http://localhost:5001

##### Remove the contatiner

```sh
make clean
```
