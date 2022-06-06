![app_python QA build](https://github.com/ananasness/iu-devops-labs/actions/workflows/qa_build.yml/badge.svg)

### How to run for production

```
docker-compose up uwsgi_django_project
```

### How to perform flake8 check

```
docker-compose up check_django_project
```

### How to run tests

```
docker-compose up test_django_project
```
