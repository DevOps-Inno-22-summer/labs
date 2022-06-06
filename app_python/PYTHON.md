# Python Best Practices

## General

Resource: [Python Best Practices – Every Python Developer Must Know](https://data-flair.training/blogs/python-best-practices/) by [Data Flair Training](https://data-flair.training/).

- Create a Code Repository and Implement Version Control
  - Inlucde a license, a README.md file, a requirements.txt, and a setup script.
- Follow Style Guidelines
  - Use PEP8 (Python Enhancement Proposals)
- Correct Broken Code Immediately
  - Always corrects bugs and defects before proceeding
- Use the Right Data Structures
- Write Readable Code
  - line breaks, code indentation, naming conventions, comments and whitespaces, maximum line length 79 characters
  - This is acheieved or supported by using a linter
- Use Virtual Environments
- Write Object-Oriented Code
- Avoid importing everything from a package
  - This pollutes the global namespace and can cause clashes.
- Don’t implement best practices from other languages.
- Do not turn off error reporting during development- turn it off after it.

## Testing

Resource: [Unit Testing Best Practices: 9 to Ensure You Do It Right](https://www.testim.io/blog/unit-testing-best-practices/) by [testIM](https://www.testim.io/).

1. Tests Should Be Fast
    1. make them as simple as possible
    1. don’t make them depend on other tests
    1. mock external dependencies
1. Tests Should Be Simple
    1. measure the cyclomatic complexity of your tests (using, for instance, a linter tool) and do your best to keep it low
1. Test Shouldn’t Duplicate Implementation Logic
    1. resist to urge to make your tests fancy
1. Tests Should Be Readable
    1. Use the Arrange, Act, Assert pattern, to clearly define the phases of your test case.
    1. Alternatively, adopt BDD-style test cases (Given/When/Then pattern.)
    1. One logical assertion per method.
    1. Don’t use magical numbers or strings in your test cases. Instead, employ variables or constants to document the values you’re using.
1. Tests Should Be Deterministic
    1. a test case should only switch its outcome (from passing to failing or vice-versa) due to a change in the production code it targets
1. Make Sure They’re Part of the Build Process
    1. make sure your (CI/CD) build process executes your unit tests and marks the build as broken when the tests fail
1. Distinguish Between The Many Types of Test Doubles and Use Them Appropriately
    1. Know the difference between stubs, spies, and, mocks, and use them wisely
1. Adopt a Sound Naming Convention for Your Tests
1. Don’t Couple Your Tests With Implementation Details
