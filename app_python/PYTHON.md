# Framework

For this project, fastapi used, as it is claims that is

1. Faster than go and nodejs
2. Makes fewer bugs
3. Robust - it gives production ready code.
4. Short - minimized code

# Best practices:

1. Folder structure - folder structured as main.py outside which is the main file of the project and core folder to save models/schemas in future and also added settings.py file inside as there can be some settings and configurations, same variables without declaring everywhere in the apps to use. Also, tests folder to add tests in future.
2. Autopep8 - linter used for automatically formatting the code and make it up to PEP8 style guide.
3. Variable names - all variable names should be lower case with underscores separating words. snake_case used for variables and camel_case used for functions and classes.

# Testing Best Practices:

1. Fast: Unit tests should run quickly as they are used to test the functionality of the application and there can be a lot of them in one project.
2. Easy to understand: Unit tests should be easy to understand to testers and developers as some companies uses tests as documentation.
3. Reliable: Tests should fail in a controlled way and should work in every environment. Tests should be reusable to avoid repeating the same tests in different places.
4. Isolated: Tests should be isolated without any dependencies on other parts of the application.
5. Avoid logic: Tests should not contain any logic. Mostly they should only test the behavior of the application without knowing implementation details.
6. Write tests during development, not after it: Unit tests are the first tests run during the development cycle and are at the bottom of the testing pyramid. As a result, they perform best when performed concurrently with development than than afterward. Some companies prefer to do unit tests before releasing production code, which is known as Test-driven Development (TDD). This exercise prepares your mind for the code's intended behavior. It raises issues and scenarios even before you start creating code, as opposed to asking them later on in the development process.
