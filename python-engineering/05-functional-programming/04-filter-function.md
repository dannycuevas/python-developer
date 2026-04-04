# `filter()` Function

- This Function will allow us to filter the results, which can also reduce the quantity of the results
- The `filter()` Function will try to receive a boolean value, so a True or False value, to tell it whether it should be "filtering the result or not" 
- For the syntax, we pass-in the Action that needs to be executed, and then the Data that the action needs to be executed upon

```python
filter(function, iterable) # also read as (function, data)
```

In other words;
- `filter()` is used to keep only the items that satisfy a condition
- `filter()` keeps items where the function returns `True`

### Example

- In this example `filter()` is going to say it is True then it is going to keep it in the List, and it is not it will remove it, or not add it to the List
- We will also need to print it as a List, to be able to print out the result back to us (the result will be only odd numbers)

```python
my_list = [1,2,3,4,5]
    
def check_odd(item):
    return item % 2 != 0 # if remainder not equal zero then it is odd number

print(list(filter(check_odd, my_list))) 

# the output:
>>>[1, 3, 5]
```

- Key note, this will create a new List for us, it will not modify the original List, keeping that "functional paradigm" in mind 
- Functions like `map()` and `filter()` are only concern with "what action to take with the item, and what should be return" 
