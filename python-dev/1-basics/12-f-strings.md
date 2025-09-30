# FORMATTED STRINGS

- Imagine you are working with a database and you are grabbing information, and it will look something like this;
```python
>>> name = 'Tomioka'
>>> age = 28
>>> print('hi ' + name + '. You are ' + str(age) + 'years old')
hi Tomioka. You are 28years old
```

- But there is a better way to do it, and that is using "formatted strings"
- We can use them by using `print(f'')` to print out our strings, and called them "f strings"

- This will allows us to no longer use symbols to concatenate our strings or converting data types to be able to print them
- Formatted Strings will just need us to use curly brackets to call our Variables to print them out

- Example of "f string"
```python
>>> print(f'hi {name}. You are {age} years old')
hi Tomioka. You are 28 years old
```
