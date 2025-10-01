# BUILT-IN FUNCTIONS and METHODS

[Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)

[Python Built In Functions](https://docs.python.org/3/library/functions.html)


# Functions

- So far we have seen only a couple of Python built-in functions thus far, here are the examples of Python built-in functions
```python
str()
int()
print()
type()
round()
```

- Using "length" will count the number of characters in our string (so the length of a string) when being printed out
```python
>>> print(len('I love my pitbull'))
17
```


# Methods

- Methods are similar to functions, but they are "owned by something"
- For example we have Python String Methods, which are specifically to use with strings 

- Short simple example of a string method - which will always begin with a simple dot (`.`)
```python
VARIABLE.format()
```

### Method Examples

- Example with an actual Variable and using `.upper()` method, to get the text in all caps
```python
>>> quote = 'to be a fighter or to be an engineer'
>>> print(quote.upper())
TO BE A FIGHTER OR TO BE AN ENGINEER
```

- The next example would do the opposite and get all the text in lower cases
```python
>>> quote = 'TO BE MARRIED OR TO GO ON DATES'
>>> print(quote.lower())
to be married or to go on dates
```

- We can also "find" specific strings of text, and display "at what index it will be", in a string Variable by using the `.find()` method
- Kinda like using Linux `grep` but inside a specific string Variable, searches the string for a specified value and returns the position of where it was found
```python
>>> quote = 'TO BE MARRIED OR TO GO ON DATES'
>>> print(quote.find('MARRIED'))
6
```

- Also, we can replace text patterns with a new one, like replacing all the occurrences of a single word for another one
```python
>>> quote = 'TO BE MARRIED OR TO GO ON DATES'
>>> print(quote.replace('MARRIED', 'single'))
TO BE single OR TO GO ON DATES
```

- Remember, the actual string Variables do not change, even after running hundreds of methods on them
- Hence the concept of "immutability", we can only create them or destroy them
- If we print our string Variable again, it will have the original value it was assigned
```python
>>> quote = 'TO BE MARRIED OR TO GO ON DATES'
>>> print(quote.replace('MARRIED', 'single'))
TO BE single OR TO GO ON DATES
>>> print(quote)
TO BE MARRIED OR TO GO ON DATES
```
