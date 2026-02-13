# PARAMETERS VS ARGUMENTS

- Generic Function
```python
def say_hello():
	print('helloooooo')
```

- The other super power of Functions is allowing us to make them "dynamic", by using the Function brackets
- We will be able to pass in "Arguments" or "Parameters" into the Functions - they are just words saying "take this Variable and pass it into the Function, in order to work with it, into the Function"

##### Parameters
- We give the "parameters" inside of the brackets of the Function name, in this case `say_hello()` for example
- We can give it parameters (or Variables) as many as we want, and use those Variables inside of the Function

### Example Function with Parameters

- We modify our simple Function to "now take 2 parameters"
	- these new 2 parameters are `name` and `emoji`, separated by a comma per each parameter
- And the print statement into an `f-String` 
```python
def say_hello(name, emoji):
	print(f'helloooooo {name} {emoji}')
```

##### Arguments
- These parameters allow us to give the Function (when we call it) what we will call as "arguments"
- **Arguments are used as the actual Values that we pass-in to a Function when calling it**
	- They are passed on separated by comma inside the brackets

- For example, calling the new Function with actual Values, as Arguments (using the same Function from above)
```python
say_hello('Daniel', ':D')
```

> NOTE:
> - Parameters are used in the block of code defining the Function
> - Arguments are the actual Values passed on when calling the Function

### Example of working Function

```python
def say_hello(name, greet):
  print(f'Hello master {name} and {greet}')

say_hello('Daniel', 'Welcome Home!')
say_hello('Bjork', 'Welcome Home!')
say_hello('Valkiria', 'Welcome Home!')

Hello master Daniel and Welcome Home!
Hello master Bjork and Welcome Home!
Hello master Valkiria and Welcome Home!
```
