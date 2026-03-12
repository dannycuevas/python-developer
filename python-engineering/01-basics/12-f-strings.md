# FORMATTED STRINGS

- Imagine you are working with a database and you are grabbing information, and it will look something like this;
```python
>>> name = 'Tomioka'
>>> age = 28
>>> print('hi ' + name + '. You are ' + str(age) + 'years old')
hi Tomioka. You are 28years old
```

- But there is a better way to do it, and that is using "formatted strings"
- We can use them by using `print(f'')` to print out our strings, and called them "f strings", this is called "string interpolation", which is a fancy way of saying "stick a Variable into a String and print it out"

- This will allows us to no longer use symbols to concatenate our strings or converting data types to be able to print them
- Formatted Strings will just need us to use curly brackets to call our Variables to print them out

##### Example of "f string":
```python
>>> print(f'hi {name}. You are {age} years old')
hi Tomioka. You are 28 years old
```


## 3 types of String Formatting

- String formatting lets you inject items into a string rather than trying to chain items together using commas or string concatenation
- As a quick comparison, consider:
```python
player = 'Thomas'
points = 33

# concatenation
'Last night, '+player+' scored '+str(points)+' points.'

# string formatting
f'Last night, {player} scored {points} points.'
```

##### There are three ways to perform string formatting:
* The oldest method involves placeholders using the modulo `%` character
* An improved technique uses the `.format()` string method
* The newest method, introduced with Python 3.6, uses formatted string literals, called **f-strings** (the one used at the beginning of this document as example)

### Formatting with placeholders

- You can use `%s` to inject strings into your print statements. The modulo `%` is referred to as a "string formatting operator".
```python
print("I'm going to inject %s here." %'something')

>>>I'm going to inject something here.
```

- Example with multiple items
```python
print("I'm going to inject %s text here, and %s text here." %('some','more'))

>>>I'm going to inject some text here, and more text here.
```

```python
print("%s %s!" %('Python','rules'))

>>>Python rules!
```

- You can even pass Variable names:
```python
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))

>>>I'm going to inject some text here, and more text here.
```

### Formatting with `.format()`

- A better way to format objects into your strings for print statements is with the string `.format()` method. The syntax is:
`String here {} then also {}'.format('something1','something2')`

- For example:
```python
print('This is a string with an {}'.format('insert'))

>>>This is a string with an insert
```

- Inserted objects can also be Variables on their own, example:
```python
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))

>>>First Object: 1, Second Object: Two, Third Object: 12.3
```
