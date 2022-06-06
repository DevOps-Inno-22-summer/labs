[![Workflow](https://github.com/heivory/DevOps-Labs/actions/workflows/workflow.yaml/badge.svg)](https://github.com/heivory/DevOps-Labs/actions/workflows/workflow.yaml)

# Moscow Time
A simple web app that displays current time in Moscow, Russian Federation.

## You need to have
1. python 3
2. docker 
3. pip

## You need to do
1. Clone repository
2. Create virtual environment
3. Install packages from requirements.txt
4. Run the app

```sh
pythom app.py
```

5. Run docker locally

```
docker build -t heivory/devops-lab .
docker run -d -p 5000:5000 --name devops-lab heivory/devops-lab
```

6. Run docker using [image](https://hub.docker.com/repository/docker/heivory/devops-lab) from docker hub

```
docker pull heivory/devops-lab:latest
docker run -d -p 5000:5000 --name devops-lab heivory/devops-lab:latest
```

## Have fun and enjoy!
