# TUPLES

- This would be our 3rd Data Structure, which is also a Data Type as well
- **A "Tuple" is like a List, but unlike a List, we cannot modify the Tuple because these are immutable, so you can think of them as immutable Lists**
	- And we will use regular parenthesis `()` to denote a Tuple (as Lists use `[]` square brackets)
	- Once an element is inside of a Tuple, it cannot be reassigned to something else
	- You can include strings, integers, and floats in tuples and access them using both positive and negative indices
	- We can also include Lists inside of a Tuple

- Here we show an example of a regular Tuple, in which we attempt to modify index 1 for a new value, but we get an error because Tuples are immutable
```python
>>> exam_tup = (1,2,3,4,5)
>>> exam_tup[1] = '5'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
    ^^^^^^^^^^^
TypeError: 'tuple' object does not support item assignment
```

- Indexing works the same - we can still extract, or print out, the values of a Tuple
```python
# -> is number 5 in exam_tup Tuple ?

>>> print(exam_tup)
(1, 2, 3, 4, 5)
>>> print(5 in exam_tup)
True
>>> print(exam_tup[3])
4
```

> NOTE HOW TO USE A TUPLE
> - If you do not need a List to change Values or items, then use a Tuple, as they have a slightly better performance so they are usually faster than Lists
