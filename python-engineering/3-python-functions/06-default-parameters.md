# Default Parameters

- First of all, "Default Parameters" will need to be defined at the Function definition, they cannot be pass-in whenever a Function is being call
- Example below, defining the default parameters with the Function definition
```python
def say_hello(name = "Rey Rojo", greet = "welcome back!"):
  print(f'Hello master {name} and {greet}')

say_hello('Daniel', 'Welcome Home!')
say_hello('Bjork', 'Welcome Home!')
say_hello('Valkiria', 'Welcome Home!')
say_hello(greet="welcome back mate", name="Jin")
```

- And so, whenever we run the Function and we forget to pass-in any arguments to it, the Function will use the default parameters as the arguments and run
```python
def say_hello(name = "Rey Rojo", greet = "welcome back!"):
  print(f'Hello master {name} and {greet}')

# say_hello('Daniel', 'Welcome Home!')
# say_hello('Bjork', 'Welcome Home!')
# say_hello('Valkiria', 'Welcome Home!')
# say_hello(greet="welcome back mate", name="Jin")
```

- This will be a great way to make sure Functions will run, even if they are called the wrong way
```python
say_hello()

>>>Hello master Rey Rojo and welcome back!
```
