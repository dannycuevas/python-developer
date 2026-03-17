# Python Scope

- "Scope" is present in the majority of languages, and it simple says "what Variables do I have access to?"
- Basically saying "Who has access to what"

### Global Scope

- When we create a new Variable, by itself, so if it not inside of a defined Function, then that Variable is part of the "Global Scope"
- Anything that is inside of a Function, it is the "Function world", its code belongs only to the Function and not to the global scope

### Scoping Order

- When printing or returning results, there is an order in which the Python interpreter will look for the values stored in Variables, like a "Scoping precedence" for example

- This will be the order the interpreter will follow:
1. Start with the local code within the Function (or any code)
2. Local parent Function
3. Global scope, meaning the current working file
4. Built-in Python Functions
