# Lab2

## Description of the best practices

- For ensuring the quality of the docker file, Docker Linter extension is used.
- I'm packiging a single app per container.
- Using slim version of python which contains the minimum packages needed from python to keep the size of the image down.
- Reducing the size of the image by adding pycache files and all files doesn't related to the source code to **.dockerignore** file. Also using **.dockerignore**  will help us avoid copying confidential or unnecessary files into the container, like configuration files, credentials, backups, lock files, temporary files, sources, subfolders, dotfiles, etc.
- Using trusted base images.
- Expose only the port that my application needs and avoid exposing ports like SSH.
- Set ENV PYTHONDONTWRITEBYTECODE=1 in Docker file to prevent python from generating pycache files and keep the container clean.
- Set ENV PYTHONUNBUFFERED=1 This is useful for receiving timely log messages and avoiding situations where the application crashes without emitting a relevant message due to the message being "stuck" in a buffer.
- Placing the commands that are less likely to change, and easier to cache, first. (Install requirments first then copying files).
- Disable the cache when install requirments to keep the Image size as small as possible.
- Using COPY over ADD since we don't need to add files from an URL or from a tar file.
- Create build file which containes only the files we want to copy to the container and use "COPY build \app" instead of "COPY . \app".  
- Grouping multiple commands together to reduce the number of layers
- There is isn't any confidential data copied to the container. We use **.dockerignore** to execlude sensetive files and settings. Also we can pass configuration via environment variables on execution "-e option in docker run" (not needed here).
- Running the containers as non-root to prevents malicious code from gaining permissions in the container host and so that not just anyone who has pulled the container from the Docker Hub can gain access to everything on the server.
- Don't bind to a specific UID for the non-root user.
- Make executables owned by root and not writable by removing chown command.
- Including healthcheck instruction in the docker file.
- Scanning the Image against vulnarabilities using "docker scan Image_name".
- Debugging our container using vscode.

## Run the image from my account and test it
