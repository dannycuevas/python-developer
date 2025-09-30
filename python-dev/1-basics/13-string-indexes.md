# STRING INDEXES

- Strings is just text, and strings are stored in memory, as an ordered sequence of characters 
- Every character is saved in place one after the other, including the spaces between characters or words

- Example of characters and the "space value"
```
'me me me'
01234567
```

- **This will allow us to get specific characters from string, called "index" by using the square brackets**

- Example
```python
>>> selfish = 'me me me'
>>> print(selfish[0])
m
```


# Start and Stop

- We can "start" getting an index, and then "stop" at a specific index space

- Example using a Variable with only numbers in it
- Going from position 0 to stop at position 3
```python
>>> selfish = '012345678'
>>> print(selfish[0:3])
012
```


# Start and no Stop

- We can also start getting an index but with no stop point
- So, just get the index starting from a specific point up until the very end

- Example without adding an stop index
```python
>>> selfish = '012345678'
>>> print(selfish[3:])
345678
```
