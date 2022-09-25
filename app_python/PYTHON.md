
Frameworks like `Django` and `Flask` can be used for a production environment, but flask is usually used for prototyping since it is easy to work with; however, flask is slow.

Also with `Flask`we have to use a lot of plugins to get a usual server functionality, that is a disadvantage.

`Django` is a [“batteries included”](https://en.wikipedia.org/wiki/Batteries_Included) framework.

For familiarity, Flask was used to write this application. 

About Python best practices, we can say:

### The code: 
- It must do what it is supposed to do.
- It must not contain defects and problems.
- It must be easy to read, maintain, or extend.

## Unit tests and best practices.

### [Unit testing best practices](https://docs.python-guide.org/writing/tests/):

- A testing unit should focus on one single functionality and prove it correct.
- Each test unit must be fully independent. Each test must be able to run alone, and also within the test suite, regardless of the order that they are called.
- Learn your tools and learn how to run a single test or a test case. Then, when developing a function inside a module, run this function’s tests frequently, ideally automatically when you save the code.
- Always run the full test suite before a coding session, and run it again after. This will give you more confidence that you did not break anything in the rest of the code.
- Use long and descriptive names for testing functions. The style guide here is slightly different than that of running code, where short names are often preferred. The reason is testing functions are never called explicitly. `square()` or even `sqr()` is ok in running code, but in testing code you would have names such as `test_square_of_number_2()`, `test_square_negative_number()`. These function names are displayed when a test fails, and should be as descriptive as possible.

### Unit tests:

There are three tests:

- `test__api_time_properly_responds()` tests that an existing api returns time properly. The returned time is from Moscow and we need to make sure the api works well to use it later in the other tests.
- `test__api_and_app__time_diff_less_than_2s()` tests that the returned time by the api and the app coincide and differ in at most 2 seconds. 
- `test_time_correctly_changed()` tests that the app in fact returns different times every time the app method `print_time()` is called and that it is displayed correctly in a browser.

