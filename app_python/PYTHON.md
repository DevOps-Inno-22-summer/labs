# DevOps Lab 1

Python framework selected is [Flask](https://flask.palletsprojects.com/en/2.1.x/). It is production ready.

A test script is included to test generating the time and the HTML.

Linter used is [pylint](https://pylint.pycqa.org/en/latest/). The missing pydocs warning is turned off; due to adequate method names.

Markdown linter is the VS Code extension [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).

## Best Practices

The article [Python Best Practices – Every Python Developer Must Know]((https://data-flair.training/blogs/python-best-practices/)) by [Data Flair Training](https://data-flair.training/) as the main resource for best practices.
Many best practices are copied as is from the article.

- Create a Code Repository and Implement Version Control
  - Inlucde a license, a README.md file, a requirements.txt, and a setup script.
- Follow Style Guidelines
  - Use PEP8 (Python Enhancement Proposals)
- Correct Broken Code Immediately
  - Always corrects bugs and defects before proceeding
- Use the Right Data Structures
- Write Readable Code
  - line breaks, code indentation, naming conventions, comments and whitespaces, maximum line length 79 characters
  - This is acheieved or supported by using a linter
- Use Virtual Environments
- Write Object-Oriented Code
- Avoid importing everything from a package
  - This pollutes the global namespace and can cause clashes.
- Don’t implement best practices from other languages.
- Do not turn off error reporting during development- turn it off after it.
