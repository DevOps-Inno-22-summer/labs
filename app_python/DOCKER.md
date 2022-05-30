# Best practices for Docker 


Most of best practices was retrieved from 
- https://snyk.io/blog/best-practices-containerizing-python-docker/
- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- https://testdriven.io/blog/docker-best-practices/

Some of most important practices: 
- Use Multi-staged builds - for better modularity (skipped in Lab 2 because project is too small)
- Order commands in Docker file appropriately
- Cache Python Packages to the Docker Host
- Separate dependencies from source code
- Run containerized Python applications with least possible privilege (and never as root)
- Find and fix security vulnerabilities (could be found by static tools)
- Run only one process per one container