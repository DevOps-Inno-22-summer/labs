# Lab3

## Description of the best practices for CI

1. Keep your Actions minimal since the longer an action takes to set up and run, the more time you spend waiting. Also plans for GitHub Actions virtual machines are limited to a hard cap of free minutes per month -- 2,000 for the free plan.
2. Avoid installing dependencies where you can. One way to do that is to take advantage of GitHub’s caching mechanism.
