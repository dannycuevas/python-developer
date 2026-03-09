# Keyword Arguments in Functions

- Remember we have the regular Parameters
```python
def say_hello(name, greet):
  print(f'Hello master {name} and {greet}')
```

- But we also have "Keyword Arguments", and they do not care about the position or order when they are being pass-in

- This is the example of using them the "regular way", and they are printing out the message in the same order as the arguments in the Function
```python
say_hello('Daniel', 'Welcome Home!')
say_hello('Bjork', 'Welcome Home!')
say_hello('Valkiria', 'Welcome Home!')

>>>Hello master Daniel and Welcome Home!
>>>Hello master Bjork and Welcome Home!
>>>Hello master Valkiria and Welcome Home!
```

- And here we use the Keyword Arguments, that as long as we use the same argument names as the Variables with values, the Function will still print out the message as how it was originally defined
```python
say_hello(greet="welcome back mate", name="Jin")

>>>Hello master Jin and welcome back mate
```
