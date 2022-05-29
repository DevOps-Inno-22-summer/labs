## Production ready framework and why I used FastAPI

Production readiness refers to when a certain application or a program will be ready to operate and be capable of handling production-level traffic, data and security. The application should be also available for all the intended users.

FastAPI framework is a modern, fast (high-performance), web framework for building APIs with Python. It is easy to learn, fast to code, ready for production.

## Description of the best practices 
- Adding license file to the repo.
- Managing python dependency using virtual environment and using pip freeze command to generate a list of Python modules and packages installed in the virtual environment to requirements.txt file.
- Adding '.gitignore' file which specifies that git should ignore files that are local to a project.
- Managing the quality of the code I'm using pylint which is static analyzer tool that analyses the code without actually running it. It checks for errors, enforces a coding standard (PEP 8), looks for code smells, and can make suggestions about how the code could be refactored
- There are two ways of getting Moscow time:
    - Depending on datetime without third-party modules
    - Using third party module called pytz

  Since our application is specified only for Moscow time. It is better to not use external library. This will help us to avoid the disadvantages that mentioned in this [article](https://www.scalablepath.com/back-end/third-party-libraries).
- For unit testing I'm using pytest 


