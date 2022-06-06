# 3

## Continuous integration

1. Code testing

* Read about best practices.
* Write unit tests for your application.
* Update a PYTHON.md ﬁle and describe your unit tests and best practices.
* Update a README.md ﬁle, add a Unit tests part.

2. Set up Git Actions CI

* Read about best practices.
* Create a CI.md and provide best practices that you found.
* Set up a Docker project.
* Automate a workﬂow.
* Optimize it, use a build cache.
* Update a README.md ﬁle.
* Add a workﬂow status badge.


### List of requirements

* Unit tests for your application
* Unit testing best practices in PYTHON.md
* Unit testing section in README.md
* Github actions CI should be present and should work
* Github actions CI should be properly organized. (build, test, push stages are present, logical structure is correct)
* Caching is present in GitHub actions
* CI.md exist and contains best practices for GitHub actions (more is better)
* The workﬂow status badge is present.

> Some additional points will be provided for implementation of best practices that you find during research and that are not mentioned in this document.

## Bonus

1. Set up Jenkins CI for your main app

* Read about best practices.
* Update the CI.md about speciﬁc Jenkins related practices.
* Use the following image to set up Jenkins:

> https://hub.docker.com/r/jenkinsci/blueocean

```
mkdir jenkins && cd jenkins
docker run --rm --name jenkins -p 8080:8080 -p 50000:50000 -u 0 -v
`pwd`:/var/jenkins_home jenkinsci/blueocean
```

> Note the admin password dumped on log. Open a browser on http://localhost:8080, run the
initial setup wizard. Choose NONE for "recommended plugins".

* Create a Jenkins Job for your app.
    * New item -> Multibranch Pipeline -> Branch Sources -> Add source -> GitHub -> repository HTTPS URL -> Save
* Create a Jenkinsﬁle in your repository.

* If it wasn't found automaticaly you can use `Scan Multibranch Pipeline Now & Log.`

![Jenkins status](./screenshots/jenkins-status.jpg) 

* Test it. Provide results as screenshots in CI.md
2. Follow steps from the main task for your extra app.
3. Set up a CI process via any another CI tool.
