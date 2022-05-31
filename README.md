# Project for DevOps course
At this point the app can only tell the current time.

## Install
From project root:
```
pip install -r app_python/requirements.txt
```

## Run tests
From `app_python` directory run:
```
pytest
```

## Run locally
`python3 app_python/app/server_prod.py`. The app will be served on port 8080.

## Run prod container locally
```
docker-compose up -d --build
```

## Run built image from Dockerhub
```
docker run --name="telltime_prod" -p 8080:8080 codeomatic/telltime:v0.0.1
```

## Access using browser
The app will be accessible on http://localhost:8080 

## Status
Lab 2 complete
