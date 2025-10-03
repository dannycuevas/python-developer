# LISTS

- This is another Data Type
- A "list" is a "Ordered Sequence of objects" that can be of any type
- Also, in Python, Lists are a form of an "Array" (a term mostly used in other programming languages)

- Lists we will denote with square brackets `[]` and "lists are mutable"
- And inside those brackets, we can have different objects, any collection of items that we want

- Here we see examples of Lists, creating a variable called `li`  and `li2` and `l3` 
- You can even mix and match different "types" (like strings, integers, floats, all together)
```python
li = [1,2,3,4,5]

li2 = ['a', 'b', 'c']

li3 = [1,2, 'a', True]
```

- Since lists are mutable (unlike strings), we can modify them on the fly, example, we will modify index 1 from laptop to desktop
```python
>>> print(amazont_cart)
['notebooks', 'laptops', 'toys', 'grapes', 'makeup', 'clothing', 'cellphone']

>>> amazont_cart[1] = 'desktop'

>>> print(amazont_cart)
['notebooks', 'desktop', 'toys', 'grapes', 'makeup', 'clothing', 'cellphone']
```

### List as a Data Structure type

- A "List" is also our first "Data Structure" that we are learning
- A "Data Structure" is a way for us to organize data together

- Example, create a variable called `amazon_cart` with multiple items in it, and then get an item based on its index position
```python
>>> amazon_cart = ['notebooks', 'watercolors', 'sodas', 'dogfood']
>>> print(amazon_cart[1])
watercolors
>>> print(amazon_cart[3])
dogfood
```
