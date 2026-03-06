# IS vs == 

### Double Equal "=="

- The double equals sign will check for "equality" or "equality of values" and types
- For example, checking equality between 2 different Data Types

```python
print(True == 1)
print('' == 1)   # empty string
print([] == 1)   # empty array/list
print(10 == 10.0)
print([] == [])   # empty arrays/lists

True
False
False
True
True
```

- Ideally when using "comparison operators" (also known as regular "logical operators") like this, you should be comparing same Data Types
	- and hopefully you are not letting Python do "type conversion" internally to "compare values" and hoping that Python figures things out for us
	- so basically, "write the most logical code" always

### "IS" keyword

- There is another way to do comparisons in Python, by using `IS` keyword, but this keyword will not work the same as `==` symbols at all

- Example using `is` in the same code, which is now all "False"
```python
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])

False
False
False
False
False
```

- So, what is different from `==` symbol?
- **Equal checks for the "equality" in the Values and "Location"**
- **So, the `is` keyword actually the equality of the Values, and checks "if the location in memory, where said value IS stored is the same as well"**
	- For example, 2 empty Lists although they are the "same thing" they live in different places in memory, so the result of comparing 2 empty Lists would be "False"

```python
print(True is True)
print('1' is '1')
print([] is [])
print(10 is 10)
print([] is [])

True
True
False
True
False
```

- Things like a List, or Data Structures, are not stored in memory in a simple way like a simple String or Integer is
- This applies even if the "exact same values" are stored, in different Variables of course, each Variable will be stored in a different place in memory
- So, `is` would not fully apply to any Data Structure, as Data Structures are stored in different places in memory, so even if their contents are "the same", when using `is` keyword they will be evaluated as `False` so in the end, they will be different things when comparing using the `is` keyword

```python
a = [1,2,3]
b = [1,2,3]

print(a is b)

False
```
