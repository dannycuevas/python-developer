# LIST UNPACKING

- In a single List, you could instead create Variables out of each item in a list
```python
a,b,c = [1,2,3]
print(a)
print(b)
print(c)

1
2
3
```

- **But then, we can also create Variables out of each item in a List, but still reserve items for a full actual List, this is called "List Unpacking"**
- This is done by separating what the Variables will be, from the actual to be List, and using the asterisk for the List name
```python
a,b,c, *my_list = [1,2,3,4,5,6,7,8,9,10]

print(a)
print(b)
print(c)
print(my_list)

1
2
3
[4, 5, 6, 7, 8, 9, 10]
```
