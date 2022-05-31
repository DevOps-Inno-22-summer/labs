# Dockerfile features

* Use small base image. There is a debate that [Alpine is not the best image for python](https://pythonspeed.com/articles/alpine-docker-python/). This seems to be true when pip starts building dependencies not present in the base Alpine.
In this case the build speed and the image size (133MB) are good.
* Use versioned packages for the base image.
* Don't use cache for base image and python pip.
* Use COPY command instead of ADD
* Specify workdir.
* Don't buffer python output
* Don't write pyc or __pycache__ files. This helps in case the container runs in readonly environment.
* Use json style CMD.
* Exclude tests folder from build
* This is prod image so we exclude server_dev.py
* Requirements install comes before application update because dependencies change not as often as code and it takes time to download them.
* Include health check
 