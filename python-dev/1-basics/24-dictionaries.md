# DICTIONARIES

- **This is a Data Type in Python, but it is also our next Data Structure**
- Remember, Data Structure is a way for us to organize data and allowing us to access that data
	- So Data Structures are like "containers" around data

- **A Dictionary will be like a List, but instead of items, they will be "key value pairs", and it will use "curly brackets" to denote it is a Dictionary, and a Dict will be an "unordered listing of key-value pairs"**
	- Unordered means that the keys (or items) are not right next to each other in memory (as in a List for example), meaning, they cannot be "sorted"
	- This means, for example; In a List, you could access its item by using the item index, in a Dict you will use the key name to access it and return its value
	- Dictionaries are "Ordered" since Python 3.7 (noted at the end of page)

- Each key value pair will be a key, like a Variable or an item, but with an actual Value assigned to it
- We separate each key-value pair with commas 

- Example of a Dictionary storing key value pairs, and then accessing one of those key values
```python
menu = {
    "coffee": 2.50,
    "tea": 2.00,
    "muffin": 3.25
}

>>> print(menu)
{'coffee': 2.5, 'tea': 2.0, 'muffin': 3.25}

>>> print(menu['muffin'])
3.25
```

> NOTE ON DICTIONARIES
> - Heads up! As of Python 3.7, they have updated this data structure to now have order maintained now. [You can read about it here](https://medium.com/junior-dev/python-dictionaries-are-ordered-now-but-how-and-why-5d5a40ee327f).  
> - However, keep in mind that dictionaries from a programming perspective have usually been unordered (and most other languages have dictionaries that are unordered).

### Key differences
- Dictionaries:
	- Retrieve objects key name
	- Unordered and can not be sorted
- Lists:
	- Retrieve objects based off locations (index)
	- Ordered sequence can be indexed or "sliced"
