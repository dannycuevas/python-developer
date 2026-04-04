# `map()` Function

- The syntax for `map()` is we pass-in a Function, and then an iterable object
- So, we pass-in the Action that needs to be executed, and then the Data that the action needs to be executed upon
```python
map(function, iterable) # also read as (function, data)
```

- We will just need a Function defined in our code, and down below whatever Function we wrote, we can call `map()` calling that Function
- In this example, in order to view the result, we have to turn it to a List as well

```python
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(list(map(multiply_by2, [1,2,3,4])))
```

- But using `map()` Function will no require to create an empty List and have the Function iterate itself
- `map()` will iterate through each item in the List we are passing-in, all we need to do is to return what effect we want to have in each item (in this case is multiply it by 2), as `map()` iterates by itself

```python
def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, [1,2,3,4]))) 
```

- The output of the newly created List from `map()` 

```python
[2, 4, 6, 8]
```

- Capitalize all of the pet names and print the list

```python
my_pets = ['sisi', 'bibi', 'titi', 'carla']  

def capitalize(string):
	return string.upper()

print(list(map(capitalize, my_pets)))
```

### Key-points 

- When you see this: `map(function, list)`
	- Just read it as: Apply this function to every item in the list
