## Best practices for development Python web application

1. Keep **documentation** clear and full.
2. Use *linters* and other **static analysis tools**, such as:
    * [*PyLint*](http://pylint.org/)
    * [*safety*](http://github.com/pyupio/safety)
    * [*bandit*](http://github.com/PyCQA/bandit)
    * [*mypy*](http://mypy.readthedocs.io/en/)
    * [*Darglint*](http://github.com/terrencepreilly/darglint)
    * [*SonarQube*](http://sonarqube.org/)
    * etc.
3. Use tested and production ready **frameworks**, such as:
    * [*Flask*](http://flask.palletsprojects.com/)  `this I used in the project`
    * [*Django*](http://djangoproject.com/)
    * [*FastAPI*](http://fastapi.tiangolo.com/)
    * etc.
4. Apply **formatting tools**, such as:
    * [*black*](http://github.com/psf/black)
    * [*isort*](http://github.com/PyCQA/isort)
    * etc.

## Best practices for unit Testing 

- Plan software Tests
- Use development practices that are Test-Oriented (TDD, patterns)
- Ensure all Tests are integrated in CI/CD pipeline
- Use proper type of testing (White-Black box, mutation, random, etc.)
- Develop requirements that are Testable