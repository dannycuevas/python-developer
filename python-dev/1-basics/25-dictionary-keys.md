# Dictionary Keys

- Dictionary Values can hold any sort of Data type... but what about the Keys?
- **Keys inside of a Dictionary will be immutable, Keys cannot change... so only Data Types that are immutable can be Keys**
	- And a Key in a Dict has to be unique, Key names cannot be repeated, or you will not able to access copies of a Key

- Inside our Dictionaries, we can have Keys that begin with numbers, or even use words like "True" for example
- And will also be possible when printing the Key Values
```python
my_book = {
  123: [1,2,3],
  True: 'yellow',
  'is_Magical': True
}

print(my_book[123])
print(my_book[True])

[1, 2, 3]
yellow
```

- So Lists cannot be Keys, because Lists can change in place
- Strings or Booleans for example, are immutable, so they can be Keys inside of a Dict 
