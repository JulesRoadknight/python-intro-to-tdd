# Notes from TDD Sessions

## What tests are good for

- Giving you confidence that the code works as intended
- Giving you a safety net to change code
- Being an easy to read manual of the purpose of the code, and how it works (if written correctly, the tests should be more informative than the code itself)

_Note: If you can delete a line of code without a test breaking, you've either got too much code or too few tests._

## TDD Concepts

### The basic idea

- Write tests that show how you want your code to work
- Fix the error given when you run the test until it passes, then stop
- Important: Take the smallest possible step to make the test pass, even if it doesn't seem meaningful or useful - it's part of the process
- AKA `First make it work, then make it good`

Example

```
test fizzbuzz_returns_one_when_given_one():
    expect Fizzbuzz.run(1) == 1
```

The simplest implementation is to make `Fizzbuzz.run(number)` always return 1, so do that. It's not useful code, but then you write a test case where `Fizzbuzz.run(number)` doesn't return 1, so you update the code.

Keep doing this until all requirements are satisfied, and make improvements when a pattern becomes visible (like repetition).

### Red, Green, Refactor

Phrasing 'the basic idea' as a looping 3 step process:

- Red: First write a test that fails
- Green: Then make it pass as simply as possible
- Refactor: Make any obvious improvements

An unspoken rule is 'get green, stay green', meaning avoid big refactors with multiple stages where the tests break.

_Note: Check that the test fails before fixing it - it's possible to write a test that always passes._

### Writing 'AAA' tests

Arrange, Act, Assert

- A guide to writing meaningful tests
- Arrange is the setup, like creating variables and initializing classes
- Act is what you do with it, usually calling a method/function that changes something
- Assert is checking that you got the expected result

Example

```
def test_#increment_increases_count_by_one():
    incident_count = 1 # Arrange
    result = increment(incident_count) # Act
    assert result == 2 # Assert
```
