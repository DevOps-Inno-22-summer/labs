# Continous Integration Best Practices

Resource: [Top 7 GitHub Actions best practices guide](https://www.datree.io/resources/github-actions-best-practices) by [datree](https://www.datree.io/).

1. Keep your Actions minimal
    1. To save time, and keep within the free plan quota
1. Don’t install dependencies unnecessarily
    1. make sure to take advantage of GitHub’s caching mechanism
1. Never hardcode secrets
    1. You can securely store secrets inside your repository’s settings, and then provide them as inputs or environment variables to your Actions at any time
1. Limit environment variables to the narrowest possible scope
    1. prevent polluting the global environment context as much as possible by always declaring environment variables with the narrowest possible scope
1. Ensure every repository contains a CI/CD workflow
1. Store authors in Action metadata to promote code ownership
1. Don’t use self-hosted runners in a public repository
    1. somebody could fork it and submit a pull request for a workflow containing malicious code
