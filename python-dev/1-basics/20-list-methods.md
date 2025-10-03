# LIST Methods

Python List methods:
https://www.w3schools.com/python/python_ref_list.asp

- You can perform a lot of different actions on Lists

- Remember that for the `len()` function, it is the actual length, it does not start counting from 0, it will do "human length"
```python
>>> basket = [1,2,3,4,5]
>>> print(len(basket))
5
```

- But Lists get really powerful when it comes to "methods"
- Remember that a "method" is an action, that is owned by something specific, and it is specific to a Data Type

#### Python has a set of built-in methods that you can use on lists/arrays.
- The way we use these "methods" is, we just add the dot `(.)` after the List name, and the method name
- **Note that Methods will modify your Lists in place, they will not create copies of the List**, so once you have modified it then you can call it for a new List Variable name

| Method                                                             | Description                                                                  |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| [append()](https://www.w3schools.com/python/ref_list_append.asp)   | Adds an element at the end of the list                                       |
| [clear()](https://www.w3schools.com/python/ref_list_clear.asp)     | Removes all the elements from the list                                       |
| [copy()](https://www.w3schools.com/python/ref_list_copy.asp)       | Returns a copy of the list                                                   |
| [count()](https://www.w3schools.com/python/ref_list_count.asp)     | Returns the number of elements with the specified value                      |
| [extend()](https://www.w3schools.com/python/ref_list_extend.asp)   | Add the elements of a list (or any iterable), to the end of the current list |
| [index()](https://www.w3schools.com/python/ref_list_index.asp)     | Returns the index of the first element with the specified value              |
| [insert()](https://www.w3schools.com/python/ref_list_insert.asp)   | Adds an element at the specified position                                    |
| [pop()](https://www.w3schools.com/python/ref_list_pop.asp)         | Removes the element at the specified position                                |
| [remove()](https://www.w3schools.com/python/ref_list_remove.asp)   | Removes the first item with the specified value                              |
| [reverse()](https://www.w3schools.com/python/ref_list_reverse.asp) | Reverses the order of the list                                               |
| [sort()](https://www.w3schools.com/python/ref_list_sort.asp)       | Sorts the list (kind of alphabetically)                                      |

- Adding, by using `append()` method, an extra item to a List
```python
>>> basket = [1,2,3,4,5]
>>> basket.append(100)
>>> print(basket)
[1, 2, 3, 4, 5, 100]
```

- We can also "insert", by using `insert()` method, a new object in a specific index of the List
- Example, insert the number 50 at index-3
```python
>>> print(basket)
[1, 2, 3, 4, 5, 100]
>>> basket.insert(3, 50)
>>> print(basket)
[1, 2, 3, 50, 4, 5, 100]
```

- To remove items from a list, by using `pop()` method, we can remove the element at the specified position
- Example, we will remove the number 50
```python
>>> print(basket)
[1, 2, 3, 50, 4, 5, 100]
>>> 
>>> basket.pop(3)
50
>>> print(basket)
[1, 2, 3, 4, 5, 100]
```

- And to remove an specific item by name, by using `remove()` method, we just need to specify the name, in this case 100
```python
>>> print(basket)
[1, 2, 3, 4, 5, 100]
>>> basket.remove(100)
>>> print(basket)
[1, 2, 3, 4, 5]
```

#### Finding an item in a List
- Check if the item you is indeed in a List, it will reply back with a Boolean
- Example, check if number 4 is in our List
```python
>>> print(basket)
[1, 2, 3, 4, 5]
>>> print('4' in basket)
False
>>> print(4 in basket)
True
```

- Or "count", with `count()` method, how many times an specific item occurs in your List
- Example, the number 3 occurs 2 times in this List
```python
>>> basket.append(3)
>>> print(basket)
[1, 2, 3, 4, 5, 3]
>>> basket.count(3)
2
```
