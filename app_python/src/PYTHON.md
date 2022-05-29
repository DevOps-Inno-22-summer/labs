# Lab1

## Production ready framework and why I used FastAPI

Production readiness refers to when a certain application or a program will be ready to operate and be capable of handling production-level traffic, data and security. The application should be also available for all the intended users.

FastAPI framework is a modern, fast (high-performance), web framework for building APIs with Python. It is easy to learn, fast to code, ready for production. It produce a neat auto-generated swagger documentation. One of the features that make FastAPI better than Flask that it is Build on ASGI (Asynchronous Server Gateway Interface) server.

## Description of the best practices  

- Adding license file to the repo.
- Managing python dependency using virtual environment and using pip freeze command to generate a list of Python modules and packages installed in the virtual environment to requirements.txt file.
- Adding **.gitignore** file which specifies that git should ignore files that are local to a project.
- Managing the quality of the code I'm using pylint which is static analyzer tool that analyses the code without actually running it. It checks for errors, enforces a coding standard (PEP 8), looks for code smells, and can make suggestions about how the code could be refactored.  
- There are two ways of getting Moscow time:
  - Depending on datetime without third-party modules
  - Using third party module called pytz

  Since our application is specified only for Moscow time. It is better to not use external library. This will help us to avoid the disadvantages that mentioned in this [article](https://www.scalablepath.com/back-end/third-party-libraries).
- For unit testing I'm using pytest.
  - I followed the Good Integration Practices mentioned in [pytest official documentation](https://docs.pytest.org/en/6.2.x/goodpractices.html).
  - For test layout, I used **Tests outside application code** layout.
- For check markdown files and flag style issues, I'm using markdownlint extension in vscode.  
- Using Run and Debug extension that vscode provide to debug our code easily.
- For monitoring Maintainability and Cyclomatic complexity of the code, I'm using [Wily](https://github.com/tonybaloney/wily?ref=morioh.com&utm_source=morioh.com).
- For check security threats in the code I'm using [Bandit](https://github.com/PyCQA/bandit).
