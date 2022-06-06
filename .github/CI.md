# CI
This CI is based on Github actions.

## Best practices
* Keep Actions minimal
* Don't install unnecessary dependencies
* Don't hardcode secrets
* Don't reinvent the while and use existing tested (and preferably verified) actions
* Use cache for things that don't change often
* Use a stable version tag when calling Actions in a workflow file
    - actions/checkout@v3
* Use explicit timeout limit

## References
* [Checkout](https://github.com/actions/checkout)
* [Cache](https://github.com/actions/cache/blob/main/examples.md#using-pip-to-get-cache-location) pip requirements
* [Setup python](https://github.com/actions/setup-python)
* Inspirational [blog post](https://blog.dennisokeeffe.com/blog/2021-08-08-pytest-with-github-actions) about Pipenv and Github actions
* Docker action [description](https://github.com/marketplace/actions/build-and-push-docker-images) and [repo](https://github.com/docker/build-push-action).
* Docker [documentation page](https://docs.docker.com/ci-cd/github-actions/) also mentions github actions.
* Release [trigger](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#release) doc