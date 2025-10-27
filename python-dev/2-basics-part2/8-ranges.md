# RANGES

- When "looping" in Python, one of the most common tools is the `range()` function
- **A `range()` is a special type of object in Python, that returns an object, that produces a sequence of Integers from start to stop**

- Example of a simple Range that goes from 0 to 100
```python
print(range(100))

range(0, 100)
```

- Ranges are super useful with Looping, you can iterate over the entire range from start to end
- Example, printing out all of the numbers in a range from 0 to 10

```python
for number in range(0, 10):
  print(number)

0
1
2
3
4
5
6
7
8
9
```

- To do something in reverse, we have to add the `-1` at the end of our range
```python
for number in range(10, 0, -1):
  print(number)

10
9
8
7
6
5
4
3
2
1
```

- Now, we create a List from a Range of 10, and convert it into 2 Lists
	- The keywords here are that we are converting this into a List, and then duplicating that List
```python
for number in range(2):
  print(list(range(10)))

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
