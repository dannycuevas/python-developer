# STRING CONCATENATION

- What does "String Concatenation" mean? it simply means combining strings (or texts) together

### Examples

- Also using a "space" character at the beginning of the name string
```python
>>> print('the sensei' + ' Dani-El')
the sensei Dani-El
```

- Using concatenation means we can "attach or rename Variables" however we like, as many times as we like
```python
x = 'Hello killers!'
x = x + ' ' + 'it is showtime!'
>>>print(x)
>>>Hello killers! it is showtime!
```

### Strings and Numbers

- While working with strings, make sure that they are all indeed strings, meaning, not trying to combine strings with numbers for example
- When trying to concatenate, make sure you are working with the same Data Types

- Example of a string with a integer, and its error
```python
>>> print('the sensei' + 12498)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
          ^^^^^^^^^
TypeError: can only concatenate str (not "int") to str
```
