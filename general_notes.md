# Easy rules

A guide from Sandi Metz is aim for 5 line methods/functions when you can. It's not always possible, sometimes it has to be 7 or 8 lines.

Similarly, 100 line classes/modules are a good target.

When either of these get much larger, it's worth checking for an opportunity to abstract

`There are only two hard problems in Computer Science: cache invalidation and naming things` - Phil Karlton

I have no idea about cache invalidation, but when it comes to naming things, the key is finding a balance between 'descriptive' and 'short'. 6 or 7 words is okay for variable/function names if needed. Avoid shortening words unless it's a well-known shortening to keep it easy to read.

Comments are okay, especially if explaining an implementation choice that might not make immediate sense. If adding two words to a function name lets you delete a comment, go for it.

The most general guideline when writing code is to ask 'is this easy to read and understand?'.

# Terms

## Abstraction

- Breaking something down into smaller, distinct parts
- In the case of code, taking a large function, class... and splitting it

Done because:

- It's easier to read and understand a smaller unit of code
- It's also easier to change
- And easier to test
