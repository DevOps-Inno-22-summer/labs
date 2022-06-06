### Best practices

* Using docker cache - all the files that change frequently are copied into image lastly so that docker cache can be used
* docker-compose.yml contains all the necessary instructions and parameters needed for app run - tech details are hidded
* secret key is generated inside a docker image

### Best practices for unit testing

* Each unit test should cover only one small chunk of functionality like function
* Each branch of if statements should be covered by a unit test
* Tests structure is the same as the project structure
* Test collected into the test classes which correspond to the bigger chunks of functionality like endpoint or class
