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

## Gilded Rose

In the case of the famous 'Gilded Rose' kata, a class handles cases for many different products, all changing the same two values 'sell_in' and 'quality'.
You are tasked with adding a new item to the inventory, which can mean adding a few more lines of code. However, changing the code (and making it longer) every time the inventory changes isn't good, so this is a prime use case for interfaces.

In the example provided, the Item class is modified to become an interface, and a class implementing that interface is created for each type of object.

All that is needed is for the required methods to be added (in this case \_\_init\_\_() and update()), and then anything else can be added as needed. An advantage of this is that for a simple case like Sulfuras, the update() call does nothing, so no other methods need implementing, while every other Item subclass adds update_quality() and update_sell_in() too. If Sulfuras added these methods, they would at best confuse the user, since they would do nothing, but be individually added anyway.

### How it works

An `Item` class can be defined, and then everything in the inventory can implement `Item`, which needs at most two methods (`update_sellin` and `update_quality`, or maybe just `update`).

You don't have to implement a formal interface, especially in languages that don't use them, as long as you use the same methods/properties.

Then `GildedRose` can be simplified to only loop through the array of Items provided, and call their update method(s), and if any items are added or removed over time, it will still work.
