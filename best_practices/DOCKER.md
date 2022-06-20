# Best practices for Docker

## Docker

- Use **trusted base image** for Python
- Use **slim image** instead of full one to reduce docker size
- Use **environment variables** to fine-tune docker for better performance
    - `PYTHONDONTWRITEBYTECODE` variable can be set to 1 to prevent Python from generating .pyc files in docker, which reduces docker size
    - `PYTHONUNBUFFERED` variable can be set to 1 to prevent Python from output buffering and allows for easier debugging
- Write `ENV` commands for one environment variable at a time to improve readability
- **Do not use common ports**, such as 8080, for your docker application to prevent possible collisions with other applications
- Package **single app per container** to improve reliability
- Leave **comments** in Dockerfile to improve maintainability and readability
- Add **app user** without root priveleges specifically to run this container to improve security
- Apply **static code analyzer** to Dockerfile. This project uses `Docker Linter` extension for VSCode
- Perform `docker scan` for **security checking**
- **Minimize** layer count
- **Frequently update** your images