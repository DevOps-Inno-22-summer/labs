# [GitHub CI actions best practices](https://exercism.org/docs/building/github/gha-best-practices).

### Set timeouts for workflows:

Many workflows don't need nearly as much time to finish, but sometimes unexpected errors occur or a job hangs until the workflow run is killed 6 hours after starting it. Therefore ***it's recommended to specify a shorter timeout***. This has the following advantages:

- PRs won't be pending CI for half the day, issues can be caught early or workflow runs can be restarted.
- The number of overall parallel builds is limited, hanging jobs will not cause issues for other PRs if they are cancelled early.

### Consider if (third-party) actions are really needed:

Actions should be treated like dependencies in your favourite programming language, they are code written by third party authors outside of the control of Exercism. Even if you trust the authors of the action, there may be a hostile takeover of the repository which will indirectly give those people access to Exercism repos, including write access. Therefore, you should carefully consider if introducing a new action is really worth it or if it's better to move the code into a (new) action under Exercism's control.

### Pin actions to SHAs: 

When using other actions, pin them to a commit (via their SHA), not to a branch or tag. This ensures that the same code will be executed each time, which is not guaranteed when pinning to a branch or tag. This has two benefits:

- It makes your build stable
- It prevents an attacker from changing a branch/tag to point to malicious code The only exception to this rule could be actions that we (Exercism) have built ourselves.

### Consider setting up a concurrency strategy

It's often not necessary or useful to run CI on intermediate commits if a newer commit has been pushed in the meantime. You can configure a [concurrency strategy](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#concurrency) in order to automatically cancel running workflows in the same context.