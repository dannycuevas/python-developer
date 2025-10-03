# MATRIX

- A "matrix" is a way to describe a 2-D List, or multi-dimensional List
- A "matrix" is a List with another List inside of it

	- This is an example of a 2-dimensional List
	- Where you have the main List (the first pair of square brackets), and the other Lists in the form of other square brackets
```python
matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
```

>NOTE:
>- This type of matrices, Lists/Arrays, come up a lot in topics like Machine Learning or image processing

### Access a Matrix List

- When accessing a matrix, we go as;
	- first call the List you want to access
	- then call the index you want to access

- In this example, we will get the 3rd list and 1st item
- And then we will get the 2nd list and 3rd item
```python
matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

>>> print(matrix[2][0])
7
>>> print(matrix[1][2])
6
```
