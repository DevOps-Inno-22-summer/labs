# Best Practices

1. Used requirements.txt file to install all the dependencies. So no other dependencies to install which can cause storage concuption.
2. Added support for non-root user.
3. Exposed only 5000 port for the app, so only necessary ports are exposed.
4. Used COPY instead of ADD, as ADD is more suitable for fetching files.
