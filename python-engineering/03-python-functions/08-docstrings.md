# DOCSTRINGS

- **"Docstrings" are Strings within a Function that will allow us to add text as if it were "documentation" (that we can also print out later whenever we want), to help us keep our code clean and easy to understand**

- This works by adding triple single quotes to open and close, example below
```python
def test(a):
  '''
  Info: this function tests and print parameter "a"
  '''
  print(a)
```

- The comments you add as "docstrings" will also display as "smart tips" within Python
- For example, if you execute `help()` in your newly define `test()` Function, you will get back the same text we were adding within the Function itself

- Example getting back the docstring
```python
def test(a):
  '''
  Info: this function tests and print parameter "a"
  '''
  print(a)

help(test)
```

- The output
```python
Help on function test in module __main__:

test(a)
    Info: this function tests and print parameter "a"
```
