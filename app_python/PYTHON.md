# Application description

The following web application is written on Python with Flask web framework. It is a simple application that shows time in Moscow. Each time when the web page is refreshed, the time is also gets updated.

## Why flask?

Flask is a production ready web framework that is used in many industrial projects successfully.
It is a very simple framework and best suited to small projects. It's also relatively fast both in terms of execution and development time.

## Best practices used
First, the application was created using PyCharm IDE with default settings. It automatically sets environment in a way that facilitates using best practices in writing Flask applications.
As a linter, one of the standard python linters - pep8 was used.    
Since the application is very small at this moment, other best practices are not used.
However, PyCharm has already created two extra folders: static and templates which is most likely going to be used in the future. 

**In terms of code (best practices of python):** 
 - I used snake case variables consistently and gave meaningful names.
 - I also tried to write the application in a way that doesn't require comments.
Modern best practices call comments as 'code smells' and the code itself should be readable, and understandable without comments (minimum comments allowed).
 - I tried to avoid reinventing a wheel, and used libraries to implement the app.
 - Also, added requirements.txt file for users to be able to install required packages without problem. It's a standard procedure in python applications to do this.
