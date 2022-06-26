# Lab3

## Description of the best practices for unit testing

1. Write Readable Tests by doing the following:
    - Have a sound naming convention for every test case. Name tests in such a way that it instantly describe the subject, what scenario is being tested, and the expected result.
    - Use Arrange, Act, Assert pattern to clearly define the test phases and enhance readability.
    - Avoid using magic numbers and replace them with constants that have readable names and explain their meaning.
2. Write Deterministic Tests which either pass all the time or fail all the time until fixed regardless how many times you run them. To ensure that the tests should completely isolated and are not dependent on other test cases. Also by controlling external dependencies and environmental values.
3. Avoid test interdependencies and not assume anything based on the order that test cases are writen . If tests are coupled together, the code should be isolated into small groups/classes to be tested independently.
4. Avoid logic in tests by avoiding Adding conditions such as if, while, switch, for, etc., which can make the tests less deterministic and readable. If including logic in a test seems unavoidable, we should split the test into two or more different tests.
5. Avoid using too many asserts in a single unit test because the rest of the assertions never get checked if one assertion is failed, resulting in an unclear vision of the test being failed. we can use parameterized tests as they enable you to run the same test multiple times with different values.
6. Automating tests in the continuous integration (CI/CD) pipeline.
