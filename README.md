# Project for DevOps course
At this point the app can only tell the current time.

## Install for local development
From project root:
```
pip install -r app_python/requirements-dev.txt
```

## Run tests
From `app_python` directory run:
```
pytest
```

## Run locally
From `app_python` directory run:
```
python3 -m app.server_dev
```
The app will be served on port 8080.

## Run prod container locally
```
docker-compose up -d --build
```

## Run built image from Dockerhub
```
docker run -p 8080:8080 codeomatic/telltime:v0.0.4
```

## Access using browser
The app will be accessible on [http://localhost:8080](http://localhost:8080/#/default/current_time_api_v1_current_time_get) 

## Status
Lab 3 in progress
