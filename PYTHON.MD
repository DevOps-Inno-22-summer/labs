# Python Best Practices

We will discuss python's best practices. Disclaimer: not all of them is used by me in the project due to unnecessity in such a small projects , but I'm showing the knowledge of them.
1. config.py file for storing application configurations
2. [virtual environments](https://docs.python.org/3/library/venv.html) for reproducible and platform-independent builds
3. [.gitignore template](https://github.com/github/gitignore/blob/master/Python.gitignore) provided by Github
4. pre-commit hooks to run the formatting tools automatically
5. [pipenv](https://pipenv.pypa.io/en/latest/) to install and manage dependencies
6. configurable [logging](https://flask.palletsprojects.com/en/2.0.x/logging/) built into Flask object

#Frameworks & Libraries
1. [Flask](https://flask.palletsprojects.com/en/2.1.x/) - a lightweight web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. Flask offers suggestions, but doesn't enforce any dependencies or project layout. There are many extensions provided by the community that make adding new functionality easy.
2. [datetime](https://docs.python.org/3/library/datetime.html) - module for manipulating dates and times.

#Why not Django or any other framework?
1. Django is too monolithic.
2. Everything is based on Django ORM.
3. Django web framework is not suitable for smaller projects and products with only a few features and requirements. Django calls for a lot of coding, which takes server processing time and bandwidth while development. 
4. Have no experience with Django.
