### Example of "list slicing"

```python
# : is called slicing and has the format
# [ start : end : step ]

# We assume this list won't mutate for each example below
my_list = [1, 2, '3', True]

len(my_list)               # 4
my_list.index('3')         # 2
my_list.count(2)           # 1 --> count how many times the number 2 appears

my_list[3]                 # True
my_list[1:]                # [2, '3', True]
my_list[:1]                # [1]
my_list[-1]                # True
my_list[::1]               # [1, 2, '3', True]
my_list[::-1]              # [True, '3', 2, 1]
my_list[0:3:2]             # [1, '3']
```

- This example, will "step-over" to every 2nd item, and will start at zero
```python
amazont_cart = [
	'notebooks',
	'laptops',
	'toys',
	'grapes',
	'makeup',
	'clothing',
	'cellphone'
]

>>> print(amazont_cart)
['notebooks', 'laptops', 'toys', 'grapes', 'makeup', 'clothing', 'cellphone']
>>> print(amazont_cart[0::2])
['notebooks', 'toys', 'makeup', 'cellphone']
```

### Copy a List to another List

- We can create clones of our Lists, so that they do not point towards one another
- This is done so each List has its own values on its own

- Example copying a list to another list using `[:]` symbols
```python
amazont_cart = [
	'notebooks',
	'laptops',
	'toys',
	'grapes',
	'makeup',
	'clothing',
	'cellphone'
]

# copy method no1
new_cart = amazon_cart[:]

# copy method no2
new_cart = amazon_cart.copy()
```
