# Debugging in Python

>**The `pdb` — The Python Debugger**
https://docs.python.org/3/library/pdb.html

- No program we write will be perfect, all programs are full of;
	- errors
	- or also called "bugs"
	- or exceptions at runtime, when the code is running
- **The act of finding and removing these errors or bugs, is called "debugging", and a big chunk of our time as programmers is "debugging code"** 

### IDE / Editors and Linting

- What is Linting? it allows us to detect, as we are coding in real time, issues with our code (like red underline in Word for grammar errors)
- This allows for "debugging" way before we are running any code 
- IDE's have linting already built-in, or by using extensions

- Also, make sure to READ the errors as they happen, sometimes Python tells you where the error is at
	- `EOL` - meaning end of line
	- `NameError` - does not know what Variable is this, or cannot find it
	- `TypeError` - Data Types not compatible
	- `KeyError` - trying to access a Key that does not exist

### Python Debugger `pdb`

- It is a built-in Module in Python, which means, part of the standard library that Python comes with
- `pbd` is the Python debugger for interactive interpreters, and it allows us to interact with the code we write 
- This is how we use `pdb` inside of a Function, to debug what values are being passed-in and double check what are we writing
	- it will take us to the terminal to enter the Variable names manually, to check what values are inside them, by using `pbd.set_trace()` Method (the most useful Method)
	- so when running, at the terminal, just type `num1` and `num2` to check the Variables

```python
import pdb

def add(num1, num2):
	pbd.set_trace()
	return num1 + num2

add(5, "askln")
```

- Also, inside the `pdb` you can type `help` command, and see a list of helpful commands in the terminal
- Try typing `list` and then `help list` to see more of what can we do
- With `a` you can see all the parameters, with their respective arguments, of the current Function that we are in into (super useful)
