# Best practices

1. .dockerignore to exclude irrelevant files.
2. Minimize the number of layers by grouping RUN, COPY and ADD instructions.
3. Use linting to detect bad practices in the Dockerfile: hadolint.
4. Use COPY instructions instead of ADD wherever possible.
5. Keep images small and standalone.
6. Avoid unnecessary dependencies.
7. Use rootless user account. Run a server as a restricted user, lowering the privileges of potentially malicious code. For this, apply the USER instruction to change the default UID from 0 to a custom one. Avoid defining users as numbers -- prefer letter naming instead.
8. Use trusted base image (official).
9. CMD instead of the ENTRYPOINT
