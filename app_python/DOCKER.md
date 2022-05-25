
# Docker best practises used

- Specify every COPY in the `Dockerfile` to avoid redundant transfers and optimize for rapid development.
- Break down `Dockerfile` commands to optimize layers to account for the most often changing files.
- Comment `Dockerfile`.
- Use [`Docker linter. VS Code extention`](https://github.com/henriiik/vscode-docker-linter).
- Use small `python:3.9-slim` base image.
- Use '.dockerignore' to avoid leaking secrets and copying unnecessary files.
- Create `root-less` user.
- Expose `ports` to be able to connect to the app from outside.
- Run `docker scan` to audit for security vulnerabilities.