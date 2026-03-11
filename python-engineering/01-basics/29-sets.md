# SETS

- Our last Data Type and our last Data Structure, at least from the main ones, the "Set"
- **Sets are unordered collections of unique objects (we cannot have duplicated objects), and they use curly brackets like a Dict, but they do not have key-value pairs, Sets just have unique values**

- Simple example of a Set, where we print out the contents of the Set
```python
>>> seto = {1,2,2,3,4,5,5,5}
>>> print(seto)
{1, 2, 3, 4, 5}
```
- Notice, Sets are collections of "unique values", even when you print them out, you will only get unique values back

- Now we will convert a regular List, into a Set, so we can print out only unique values using the Set, instead of printing everything out like we would with a regular List
```python
>>> nums = [1,2,2,3,4,5,5,5]
>>> print(set(nums))
{1, 2, 3, 4, 5}
```

- We cannot search indexes in a Set, but we can check if a item does exist in a Set
```python
>>> seto = {1,2,2,3,4,5,5,5}
>>> print(seto)
{1, 2, 3, 4, 5}

>>> print(seto[2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    import platform
          ^^^^^^^
TypeError: 'set' object is not subscriptable

# -> is number 4 in nums Set ?
>>> print(4 in seto)
True
```

### Basic exercise

- Write an expression that would turn the String `Mississippi` into a Set, thus having only unique letters
- Solution:
```python
set("Mississippi")
```

- Remove duplicates with the `set()` function, resulting in a Set that only contains unique values
- This demonstrates how Sets in Python automatically filter out duplicate entries
```python
set([1,1,2,3])
>>>{1, 2, 3}
```
