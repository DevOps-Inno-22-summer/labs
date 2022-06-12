# Lab3

## Description of the best practices for CI

1. Using Self-Hosted Runners in GitHub Actions Workflows.
2. Leveraging GitHub Actions Marketplace
3. Keep your Actions minimal since the longer an action takes to set up and run, the more time you spend waiting. Also plans for GitHub Actions virtual machines are limited to a hard cap of free minutes per month -- 2,000 for the free plan.
4. Avoid installing dependencies where you can. One way to do that is to take advantage of GitHub’s caching mechanism [here](https://github.com/actions/setup-python#caching-packages-dependencies).
5. Never hardcode secrets in yml file and securely store secrets inside your repository’s settings, and then provide them as inputs or environment variables to your Actions at any time.
6. Limit environment variables to the narrowest possible scope to prevent polluting the global environment context as much as possible.
7. Store authors in Action metadata to promote code ownership.
