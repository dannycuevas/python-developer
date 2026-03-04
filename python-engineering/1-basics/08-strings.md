# STRINGS IN PYTHON

- "String" will be known as `str` in Python
- A String is simply a piece of text

- You can do strings with quotation marks, and also with double quotes
- And anything can go inside the quotes, including symbols
```
'hello there 1982@!$'
"also hello there (#$#)"
```

- You can confirm you are working with a string by getting its "type"
```python
>>> print(type("hi hello 12389!@$ "))
<class 'str'>
```

# Working with Strings

- We can also have "long strings" that will allow us to work with large portions of text
- These will use triple single quotes 

- Example of a Variable that will have a long string inside it
```python
long_variable = '''
wow
0 0
---
somebody was wowed
'''


>>> print(long_variable)

wow
0 0
---
somebody was wowed
```

- Now with another example of strings, we will display a full name, that was previously built in pieces
```python
>>> first_name = 'Daniel'
>>> last_name = 'Cuevas'
>>> full_name = first_name + ' ' + last_name
>>> print(full_name)
Daniel Cuevas
```
