# Project features
* Use [fastapi framework](https://fastapi.tiangolo.com/). It is fast, production ready, provides builtin generated api interface, and uses python typing system for validation.
* Configure versioned urls. It is important for apis in order to keep backward compatibility.
* Fast and prod ready ASGI server [uvicorn](https://www.uvicorn.org/)
* Enable different running configuration for prod and testing without changes to the main codebase.
* Enabled pytest
* Separate dev and prod requirements

# Unit tests
* Use pytest with fixtures
* Test directory is separate from the codebase
* Tests are fast
* Test only code relevant to the project
* Predictable and consistent behavior in tests (use freezegun to deal with time)