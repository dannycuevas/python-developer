# Functions using Logic

- Now that we understand Data Types like Strings, Integers, List, etc, and we also know "conditional statements", For and While loops, we can being adding "logic" statements to our Functions

- In this example, we will create a Function that will iterate inside a List and check for ANY even numbers

```python
# return True if any number is even inside of a List
# the parameter we are passing-in is assumed to be the List
def even_list(num_list):
  for number in num_list:   # check FOR every item inside my object (this List)
    if number % 2 == 0:   # if any item mod 2 is equal to zero
      return True   # then return True
    else:   # if none found, then
      pass   # keyword "pass", so do not do anything
```

```python
# now we pass-in a List with even numbers to make sure it works
even_list([2,4,5])

>>>True
```

>NOTE
>- Listed much more examples in Jupyter notebook 4
