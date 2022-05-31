# Best practices for Git Actions CI

1. Keep your Actions minimal.
2. Don’t install dependencies unnecessarily.
3. Never hardcode secrets, for github you can store it in settings of your project.
4. Limit environment variables to the narrowest possible scope.
5. Ensure every repository contains a CI/CD workflow, it is more important for companies, where there are a lot of repositories.
6. Store authors in Action metadata to promote code ownership. This point is also more important for companies, because now I am only one developer.
7. Don’t use self-hosted runners in a public repository.
