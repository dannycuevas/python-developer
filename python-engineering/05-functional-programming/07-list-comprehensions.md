# List Comprehensions

- We will be able to use "comprehensions" with these 3 data types; Lists, Sets, Dictionaries
- "Comprehensions" are a quick way for us to create Lists or Sets or Dictionaries, instead of perhaps "looping" or "appending" a bunch of "items" to Lists'
- Comprehensions syntax:
```python
my_list = [param for param in iterable]
```

- Take a look a this simple example of creating a new List out of the characters of a String, we will see if we find a way to simplify this

```python
my_list = []

for char in "hello":
    my_list.append(char)

print(my_list) 

>>>['h', 'e', 'l', 'l', 'o']
```

- So, following the basic syntax, we create the same code but in one line only
	- we basically create a Variable, the first `char` in the expression
	- and then it reads "for each `char` in the `iterable`" 
	- then add that to the List

```python
my_list = [char for char in "hello"]

print(my_list) 

>>>['h', 'e', 'l', 'l', 'o']
```

- Now we see the same example, this time with number, grabbing all of the numbers from a range of 0 to 50, and append all of them to a new List

```python
my_list2 = [num for num in range(0,50)]

print(my_list2)

# the output:
>>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
```

- This time we want the same action, but every number will be multiplied by 2
	- we will use the same For Loop `for num in range(0,50)`
	- but instead of just the Variable `num` it is now an "expression" of how we want to act upon each number

```python
my_list3 = [num*2 for num in range(0,50)]

print(my_list3)

#the output
>>>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
```

- Following the same example, but now the numbers are to the power 2, and we only keep the "even" numbers

```python
my_list3 = [num**2 for num in range(0,50) if num%2 ==0]

print(my_list3) 

# the output:
>>>[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304]
```

### Exercise

- This next code, that we have done before, will only print out a new List with only duplicated values, if they were not already existing in the new List

```python
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)
```

- **We want to use a Comprehension and do just one line of code, how do we do it?**
	- we do not need to modify the original first Value, so it stays as `item` at the very beginning 
	- then we loop over `for item in some_list` 
	- and we want to only add the items that are repeated `if some_list.count(item) > 1`  
	- but we only need the items once, not all the times that they are repeated
	- we wrap the entire List to turn it into a Set, using the `set()` Function from Python built-in Functions (for Type conversion), and it will result into an actual Set with curly braces as result = `{'n', 'b'}` and we want a List 
	- so now we just create a List out of that Set, same way, we wrap it with the `list()` Function for Type conversion as well, so we finally print out a List with the results

```python
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplica = list(set([item for item in some_list if some_list.count(item)>1]))

print(duplica)

# the output
>>>['n', 'b']
```
