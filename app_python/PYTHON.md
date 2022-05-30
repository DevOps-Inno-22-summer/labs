# Lab 1

For production ready envoirnment, Python [Flask](https://flask.palletsprojects.com/en/latest/) is used.

MarkdownLint is used as VSCode extension.

## Best Practices

The blog [Python Best Practices to Follow in 2022](https://aglowiditsolutions.com/blogpython-best-practices/) by [AgloWild](https://aglowiditsolutions.com/) provides us with some best practices that we should consider.

+ First thing to consider is to choose meaningful name for class, variable and functions.

+ Properly structure your repository and following components should be in your repository.
  + Licences, README file, Module code, setup.py, requirement.txt, Documentation and Tests.

+ Imports should be orginized. Put a blank line between each group of imports. It should have following order.

  + Standard Library imports.

  + Related Third-party imports.

  + Local application/library specific imports.

+ Use comments always and keep your comments updated with your updation of code. You can use following types of comments.
  
  + Single line comments.

  + Multiline comments.
  
  + Docstring comments.

+ Test code frequently to detect and ensure that not faulty code is being build.

+ Avoid creating global variable.

+ Exception handeling.  

+ Code should be explicit.

+ Code in Idiomatic way.

  + Use Unpacking, try using enumerate() to assign or references to items while unpacking.

  + Use thrwoaway variables while you trying to assign but will not need variable, you can use __.
