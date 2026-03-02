# "args"

- The `*args` and `*kwargs` are 2 "functional parameters",  notice the "stars" in their name too
	- They stand for "arguments" and "keyword arguments"
- If you work with Python Functions long enough, they will allow you to find a way to;
	- **"Accept an arbitrary number of arguments and keyword arguments without having to predefined a bunch of parameters in your Function calls"**

- Example creating a Function with which we can pass-in as many arguments as we want
- We will be getting back the 5% of the sum quantity 
```python
def myfunction(*args):
	return sum(args) * 0.05
```

- By default, Python is going to take all the parameters that are passed-in, and set them to be inside a Tuple
```python
myfunction(40,60,100,50)

>>>12.5
```

- The next example will just print out all of the arguments we are passing in
```python
def myfunc(*args):
  for item in args:
    print(item)

myfunc(37,3984,3849,234,3)

>>>37
>>>3984
>>>3849
>>>234
>>>3
```

- Another example;
	- define a function called `myfunc` that takes in an arbitrary number of arguments
	- and returns a List containing only those arguments that are even
```python
def myfunc(*args):
    evens = []
    for item in args:
        if item % 2 == 0:
            evens.append(item)
    return evens
```

# "kwargs"

- Python offers a way an arbitrary number of "key-worded arguments"
- So, instead of creating a Tuple of Values, `**kwargs` will build a Dictionary of key-value pairs
	- Meaning `kwargs` will return back Dictionaries, that you can then play around inside of your Function

```python
def myfunc(**kwargs):
  if "fruit" in kwargs:
    print("My fruit of choice is {}".format(kwargs["fruit"]))
  else:
    print("I did not find any fruits here")
```

```python
myfunc(fruit="Apple", veggie="Corn")

>>>My fruit of choice is Apple
```

### Combined example

- The next example will show how we can use both `args` and `kwargs` together in a single Function
- We are still defining the exact Values we want to get back in our result, and as defined in out Function parameters;
	- All "arguments" `args` first
	- Then all "keyword arguments" `kwargs` next

```python
def myfunc(*args, **kwargs):
  print("I would like {} {}".format(args[0], kwargs["food"]))
```

```python
myfunc(10, 20, 30, 40, fruit="orange", food="bacon", animal="bat")

>>>I would like 10 bacon
```
