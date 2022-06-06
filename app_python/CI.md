# Best Practices For Git Actions CI

- Keep your actions **minimal**
    - Use **lightweight distributives** for docker
    - Don’t install excessive dependencies
- **Never hardcode** secrets
- Create **separate environments for secrets** to limit access scope
- Limit environment variables to the **narrowest possible scope**
- **Don’t use self-hosted runners** in a public repository, as a pull request with malicious code can compromise your host
- Don’t use uncertified actions, as they can contain malicious code