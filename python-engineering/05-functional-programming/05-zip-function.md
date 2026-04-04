# `zip()` Function

- For the `zip()` Function we will need two Lists (so 2 iterables) and we can "zip them together"
- The syntax can use as many iterables as we want
- `zip()` will iterate over each List item, or Data Structure item, and zips them together 

```python
zip(iterable1, iterable2, ...etc)
```

### Example `zip()` Function

- This example will use 2 different List to zip them together

```python
my_list = [1,2,3,4,5]
your_list = [10,20,30]

print(list(zip(my_list, your_list))) 
```

- The output

```python
[(1, 10), (2, 20), (3, 30)]
```
