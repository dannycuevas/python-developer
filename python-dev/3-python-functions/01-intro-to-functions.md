# INTRO TO FUNCTIONS

- Creating clean repeatable code is a key part of becoming an effective programmer
- Python "**Functions** allow us to create blocks of code that can be easily executed many times, without needing to constantly rewrite the entire block of code"
- It is very important to get practice combining everything you’ve learned so far (control flow, loops, etc.) with functions to become an effective programmer

# Define a Function

- Creating a function requires a very specific syntax, we will define a block of code that forms our Function using `def` keyword, which means "define", it will also need correct indentation, and proper structure
- After the `def` keyword, we give it a name, and Functions will use the same naming conventions we use with Variables 
- And after the name, we use the "brackets", to let the interpreter know this is something we are going to perform an action on, or that this is something that is going to perform an action on a Data Type
- Lastly, add the action within your block of code
```python
def name_of_function():
	’Docstring explains function.’
	print(“Hello”)
```

```python
def say_hello():
	print('helloooooo')
```

- After we have define our Function, we will call it by using the brackets
```python
say_hello()

helloooooo
```

- This is the power of Python, creating our own Functions, and calling them as many times as we want in our codebase 
- Just remember that the interpreter runs line by line, from top to bottom, so the Functions need to be define above, and from there on below, be called as much as you want
