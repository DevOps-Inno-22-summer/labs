# GitHub Action CI/CD best practices
- Keep your Actions minimal
- Don’t install dependencies unnecessarily
- Never hardcode secrets
- Limit environment variables to the narrowest possible scope
- Ensure every repository contains a CI/CD workflow
- Store authors in Action metadata to promote code ownership
- Don’t use self-hosted runners in a public repository
- Use specific action version tags
- Don’t use plain-text secrets
- Only run workflows on trusted code