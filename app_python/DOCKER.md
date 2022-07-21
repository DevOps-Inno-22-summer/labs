# Docker best Practices

1. Added only required files for building (extra files might slow down builds)
2. Used requirements.txt file list all the requirements needed for python application
3. Only exposed port 5000 which is used by the python application
4. Prefer COPY to ADD
5. Add .dockerignore to exclude unnecessary files and folders
6. Do multi stage builds