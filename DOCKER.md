# Docker Best Practices

The resource used is the official Docker documentation best practices guides for [Docker development](https://docs.docker.com/develop/dev-best-practices/), [creating Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/), and [image building](https://docs.docker.com/get-started/09_image_best/). Many best practices are copied as is from the guides.

1. Keep images small
    1. Start with an appropriate base image
    1. Use multistage builds
    1. Consider creating your own base image
    1. Always use useful tags when building images
1. Persisting appication data
    1. Avoid storing application data in your container’s writable layer using storage drivers.
    1. Use secrets to store sensitive application data used by services
    1. Use configs for non-sensitive data such as configuration files
1. Use CI/CD for testing and deployment
1. Create ephemeral containers
1. Exclude with .dockerignore
1. Using multi-stage builds to
    1. Install tools you need to build your application
    1. Install or update library dependencies
    1. Generate your application
1. Don’t install unnecessary packages
1. Decouple applications
1. Minimize the number of layers
1. Sort multi-line arguments (alphanumerically)
1. Leverage build cache
1. Security scanning images using `docker scan`
