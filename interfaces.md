# Interfaces

While some languages implement interfaces directly (like Java, see https://www.w3schools.com/java/java_interface.asp), many that don't still allow you to use them indirectly with something called duck-typing.

_If it walks like a duck and quacks like a duck, then it's probably a duck._

Duck typing means that as long as one class contains the same methods and attributes as another, you can use them interchangeably.

For example, if you have two classes `User` and `Admin`, and both of these classes implement `id()`, `security_level()`, `validated()`, and `delete_user()` methods, as well as having the `id`, `validated`, and `security_level` attributes, then you could pass either `User` or `Admin` as a parameter to method `checkUserValidation()`, and it will work for both of them, even though they are different classes.

```
def checkUserValidation(user):
    return user.validated()
```

Both `User` and `Admin` implement `validated()`, so both can be passed to `checkUserValidation()` to have the method called.
