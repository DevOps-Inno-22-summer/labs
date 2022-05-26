# Best Practices

- Use **`.dockerignore` file** to prevent getting unnecessary files in the image.
- Use **`COPY` instead of `ADD`**. It saves from unexpected unzip.
- Use **trusted base images**. We use official python image.
- Package a **single app per container**. It is more reliable.
- Make **comments** in Dockerfile. It improves maintainability and readability.
- Add **root-less user**.
- **Static analyzes** of Dockerfile. We use `hadolint` linter for it.
- Make `docker scan` for **security checking**.
- **Minimize** number of **layers**.
- **Update** your images **frequently**.
