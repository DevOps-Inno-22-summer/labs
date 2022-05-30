### Best practices

* Using docker cache - all the files that change frequently are copied into image lastly so that docker cache can be used
* docker-compose.yml contains all the necessary instructions and parameters needed for app run - tech details are hidded
* secret key is generated inside a docker image
