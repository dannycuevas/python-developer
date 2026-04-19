# PYTHON BUILT-IN MODULES

>**Python Module Index**
https://docs.python.org/3/py-modindex.html

- Python is extremely useful through what we call "external modules and packages", and entire package system, where we can borrow and expand on the Python functionality 
	- and these, are called "built-in Modules"
	- these modules were installed when we downloaded the Python interpreter, or "Anaconda" 
	- but in order for us to use them, we have to "import" them
	- in other languages, these may be called "standard library"
- **Having the ability to import built-in Modules into your code using Python, and have access to more features to write code, will also be known as "standard library" (since we are calling in more functionality "internally")** 

```python
import random # import the module to current working file
print(random) # print out the local location of this module
help(random) # get the documentation for this module
```

- Once you have imported a Module, you can read that Module documentation by using the `help()` Function
```python
import random
help(random)
```

### Examples

- And then use `dir()` Function, to check of all of the Methods available on that package

```python
print(dir(random))
```

- For example, use the method `.random()` to get a random number from zero to 1

```python
import random
print(random)
print(random.random())

# the output

<module 'random' from 'c:\\ProgramData\\anaconda3\\Lib\\random.py'>
0.8128308921127514
```

- Now, generate a random integer, and give it a number from where to start off and another number where it should end

```python
import random
print(random)
print(random.randint(1, 50))

# the output

<module 'random' from 'c:\\ProgramData\\anaconda3\\Lib\\random.py'>
47
```

- Another example, is to `.suffle()` a List

```python
import random

my_list = [1,2,3,4,5,6,7]
random.shuffle(my_list)
print(my_list) 

# the output

[6, 5, 3, 4, 1, 2, 7]
```
