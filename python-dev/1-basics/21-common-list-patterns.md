# COMMON LIST PATTERNS

### Reversing Lists

- We can organize a List with `.sort()` method
- Then reverse it `.reverse()`
- And then "reverse slicing" by using a slicing method `list[::-1]`
	- This last one, with the slicing method, will create a new List but it will not persist

```python
>>> basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

>>> basket.sort()
>>> print(basket)
['a', 'b', 'c', 'd', 'd', 'e', 'x']
>>> basket.reverse()
>>> print(basket)
['x', 'e', 'd', 'd', 'c', 'b', 'a']
>>> print(basket[::-1])
['a', 'b', 'c', 'd', 'd', 'e', 'x']

>>> print(basket)
['x', 'e', 'd', 'd', 'c', 'b', 'a']
```

### List Range

- We can create a "range" of objects, and then turn that into a List
- Think of it like "automating" the creation of simple Lists, specially a numbered List

```python
>>> print(list(range(1, 100)))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
```

### The Join method

- "Join" is actually something that works on strings, it is a string method
- This method will allow you to add more items, as in the form of a List, to your string
	- In order words, this work as if turning a List into a String
- Remember, that the method will be actually creating a new object, so just assign it a new Variable name to be able to print it out

```python
sentence = ''

new_sentence = sentence.join(['hello', 'world', 'my', 'name', 'is', 'python'])

print(new_sentence)

helloworldmynameispython
```

- And then use the original string as a item that will be between each item of the `.join()` method

```python
sentence = '@'

new_sentence = sentence.join(['hello', 'world', 'my', 'name', 'is', 'python'])

print(new_sentence)

hello@world@my@name@is@python
```
