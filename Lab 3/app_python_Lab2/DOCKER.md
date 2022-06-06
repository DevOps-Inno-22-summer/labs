# Lab 3

## Best Practices

The blog [Docker Best Practices for Python Developers](https://testdriven.io/blog/docker-best-practices/) provides us with best practices that we should follow.

+ Use multistage builds to create leaner and more secure docker images.

+ Order Dockerfile commands Appropriately to leverage layer caching.

+ Use small docker base images for modularity and security.

+ Minimize number of layers. It's good idea to add RUN, COPY, and ADD commands.

+ Use unprivileged containers.

+ Cache Python packages to docker host. As requirements file is changed, the image needs to rebuild to install the new packages.

+ Run only one process per container.

+ Don't store secretes in Images.

+ Use a .dockerignore file.

+ Lint and scan your dockerfiles and Images.

+ Use python virtual envoirnment inside a container.
