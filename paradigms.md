# Programming Paradigms

There are fundamentally different approaches to programming, largely dependent on the language (Haskell is strictly functional, C++ is object-oriented, BASIC is imperative, Python can be anything).

It's not vital to understand paradigms thoroughly, it just helps to be able to identify imperative code as a refactoring opportunity in a functional or object-oriented codebase.

## Terminology

### Mutating

Changing part of the data.

#### Is mutating when:

- Adding/removing/editing a field in an object
- Changing the values of an object

E.g. changing the 'age' value of a user object

user_data = {
~~'age': 99~~ 'age': 100,
'id': 6070,
'email': 'test@email.com'
}

#### Is not mutating when:

- Replacing the entire object with a different object

E.g. Replacing `user_data` with the same data, but the `age` value is different

```
user_data = {
    'age': 99,
    'id': 6070,
    'email': 'test@email.com'
}
```

with this:

```
user_data = {
    'age': 100,
    'id': 6070,
    'email': 'test@email.com'
}
```

## Imperative programming

- Like writing a switchboard or a flowchart
- Handles specific cases with 'if' and 'switch' statements to control flow
- Common when writing shell scripts and command-line applications

## Functional programming (FP)

- Creates stateless functions
- May have a container module - like a class
- Functions always return output
- Functions never use external information (like class state) to produce the result
- Aims to eliminate 'side-effects' by never changing anything outside of the function
- Given the same input, you should always get the same output
- Functional programming tends to avoid mutating data
- Functions often return the entire data structure to enable chaining e.g. `a(user).b.(user).c(user)`

## Object-oriented programming (OOP)

- Creates classes that are initialized with state
- Instead of functions that return the updated state, there are methods that update state stored in the initializer
- Uses methods in those classes to mutate the state and achieve the final result
- The same input may not always get the same output, since methods can use external data
