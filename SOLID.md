# SOLID Principles

- A set of 5 principles to be used as guidelines
- The first one is the most important

In brief:

## Single Responsibility Principle

Everything should have one purpose (this class contains methods that update the database, that function tells you whether or not input is valid)

## Open/Closed Principle

Code should be closed to modification, but open to extension. This means make the code modular so instead of changing existing files, you should be able to add separate files to extend functionality (in short, add more files, not more lines)

## Liskov Substitution Principle

The least helpfully named, this principle refers to interchangability of code through subtypes. If `PremiumUsers` is a subtype of `Users`, then you should be able to use `PremiumUsers` anywhere that you would use `Users` (if they share the same methods and properties, then who cares?). This doesn't apply both ways.

## Interface Segregation Principle

No code should be forced to depend on methods it does not use. Something implementing an interface must have every method the interface does, which is fine when they're all needed.
However, if the interface grows to become too broad, methods may end up being implemented that the programmer knows will never be used.
To avoid this, interfaces should be kept small and specific so that every method it contains is used by all of its dependents.

## Dependency Inversion Principle

The `let's not hard-code this` principle. If it is possible to inject a dependency as a parameter rather than hard-coding it, then do so.

For example, if class `A` requires an instance of class `B`, then pass the instance `b` in as an argument when needed instead of instantiating `b` as part of `A`, which will then break if `B` is moved or deleted.
