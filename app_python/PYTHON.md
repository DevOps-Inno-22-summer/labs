# Best practices

## General project practices

- Use the **KISS principle** during design process
- Employ **TDD (test driven development)** process
    - For testing, this application uses `unittest`
    - 
- Use **version control system**. This application uses **Git**
- Use **licence file** to describe legal part of the project. This project is distributed under **MIT licence**
- Use **static code analyzers** during development. This project uses linters through `Linter` extension for VSCode, which supports all of the used languages (Python, Markdown, HTML)
- Keep tests in a separate folder to declutter project

## Python

- Use **PEP8 standart** for code formatting
- Provide project requirements via `requirements.txt` file
- Use **docstrings** for code documentation
    - For docstring generation streamlining, `autoDocstring` extension for VSCode is used
- Use **PyPI** instead of manual installation for package management
- Follow **The Zen of Python** principles
- **Avoid full-package imports** if possible

## Unit testing

- Use **uniform naming pattern** for tests. In this application, `test__tested_function__expected_behavior` pattern is used
- One unit test check only **one program functionality**
- Test should be easily **readable and concise**
- Test should only contain **one assert**
- Assert should return **error message** on fail, preferrably a custom one
- Multiple tests should be able to be executed in **any combination and order**

## HTML

- Use code formatter for better readability. This project uses `Prettier` extension for VSCode