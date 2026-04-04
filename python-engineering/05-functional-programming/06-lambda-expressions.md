# "lambda" Expressions

- "Lambda" is actually a computer science term, that really is compatible with this idea of Functional Programming 
- Lambda Expressions, in Python, are one-time anonymous Functions that you do not need more than once
	- Lambda expressions are really useful when you are using them for Functions that you only use once ever
	- and anonymous Functions do not need to be named since they only run once

- Lambda syntax from the tool tip, and below a different example of how to look at the syntax

```python
# 1- regular syntax
lambda [parameters] : expression

# 2- different look at the syntax
lambda parameters : action(parameters)
```

### Example 1

- This is a simple example of grabbing a List of numbers, and multiply each number in the List by 2 with a single line of code
- This example demonstrates how we will not need to write a whole Function by itself, as we only need to run this code once
- What are we doing in this code? it takes an "item" from the List, and then that "item is multiplied by 2"

```python
my_list = [1,2,3,4]

print(list(map(lambda item : item*2, my_list)))

# the output:
>>>[2, 4, 6, 8]
```

- `map()` applies a function to every item in a list
	- effectively saying - take the lambda function apply it to every `item` in the List `my_list`

|Item|Lambda|Result|
|---|---|---|
|1|1*2|2|
|2|2*2|4|
|3|3*2|6|
|4|4*2|8|
- Next, In Python 3, `map()` does not immediately produce a list, it produces a map object (iterator), something in a place in memory (not visible to us humans)
- To actually see the results, we convert it to a list: `list(map(...))`
- What is happening step by step?;

| Step | Action                              |
| ---- | ----------------------------------- |
| 1    | Python reads `lambda item: item*2`  |
| 2    | `map()` applies it to each item     |
| 3    | `map()` produces results one-by-one |
| 4    | `list()` collects them              |
| 5    | `print()` shows the list            |

- In modern Python, people prefer list comprehensions
- Instead of:
```python
list(map(lambda item: item*2, my_list))
```

- Most engineers write:
```python
[item*2 for item in my_list]
```

- Example:
```python
my_list = [1,2,3,4]

print([item*2 for item in my_list])
```

### Example 2

- Now, we will use another example running `filter()` Function
- This time we want to get back only odd numbers

```python
my_list = [1,2,3,4]

print(list(filter(lambda item : item%2, my_list)))

# the output:
>>>[1, 3]
```

- `filter()` is used to keep only the items that satisfy a condition
	- `filter()` keeps items where the function returns `True`
	- In this case, it keeps the odd numbers
	- This calculates the remainder when dividing by 2, saying “Keep the numbers where `item % 2` is not zero”

|Number|item % 2|Meaning|
|---|---|---|
|1|1|True → keep|
|2|0|False → remove|
|3|1|True → keep|
|4|0|False → remove|

- What is happening step by step?;

|Step|What Happens|
|---|---|
|1|Python reads the lambda|
|2|`filter()` applies it to each item|
|3|Only items returning `True` are kept|
|4|`list()` converts the results to a list|
|5|`print()` displays them|

- Just like with `map()`, Python developers usually prefer list comprehensions
- Instead of:
```python
list(filter(lambda item: item % 2, my_list))
```

- Most engineers write:
```python
[item for item in my_list if item % 2]
```

- Example:
```python
my_list = [1,2,3,4]

print([item for item in my_list if item % 2])
```

- Quick comparison

|Method|Code|
|---|---|
|filter + lambda|`list(filter(lambda x: x%2, my_list))`|
|list comprehension|`[x for x in my_list if x%2]`|
