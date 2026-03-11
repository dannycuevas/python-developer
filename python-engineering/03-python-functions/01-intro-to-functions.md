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

>>>helloooooo
```

- This is the power of Python, creating our own Functions, and calling them as many times as we want in our codebase 
- Just remember that the interpreter runs line by line, from top to bottom, so the Functions need to be define above, and from there on below, be called as much as you want

# Print VS Return

- When using Functions, we will not really see a lot of `print()` statements inside of a Function
- Typically, we will use the `return` keyword to send back the result of the Function, instead of "printing it out"
- Keyword `return` will allow us to save, or assign, the output of the Function to a new Variable, and it will not require and of the parenthesis symbols "`()`"
	- unlike `print()` that does not "save" the outputs
	- this will allow us to call (anywhere else in your code) that Variable that is storing the output

### Example Function with `return`

- Example using an "add Function", that takes in 2 arguments or parameters `num1` and `num2` 
	- then it is going to "return" the sum of those 2 Variables - like allowing us to store the results
	- we then assign that "return result" to a Variable
	- finally, we then "print" that final Variable
```python
def sum_numbers(num1,num2):
  return num1+num2

result = sum_numbers(2,3)
print(result)

>>>5
```

### Another analogy (real life)

#### `print` is like:
🗣️ Saying something out loud
> “The total is 100.”
- But no one wrote it down.

#### `return` is like:
✍️ Writing something on paper and handing it over
> “Here is the total: 100.”
- Now it can be reused, stored, or passed along.

### Golden beginner rule ⭐

> **Use `print()` to see things.  
> Use `return` to build things.**

At this learning stage:
- It’s OK to use `print` a lot    
- But real programs depend on `return`
