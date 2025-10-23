# LOGICAL OPERATORS

- A Logical Operator allows us to perform logic between 2 things
```python
is_friend = True
is_hostile = False

if is_friend or is_hostile:
	print('best friends forever')

>>>best friends forever
```

- Examples of logical operators in Python
```python
>
<
== # this is called "equal to"
= # 1 equal is used to "assign a variable"
!= # this is "not equal to"
```

- Quick example
```python
print(5 > 10) # is 5 greater than 10?

>>>False

print(5 == 5) # is 5 equal to 5?

>>>True

print(1 >= 0) # is 1 greater than or equal to 0?

>>>True
```

### Exercise

```python
is_magician = True
is_expert = False

# if this person is both magician and an expert, print this
if is_magician and is_expert:
  print('you are a master magician')

# otherwise, if this person is a magician and not an expert, print this
elif is_magician and not is_expert:
  print('at least you are getting there')

# otherwise, and if you are not a magician, print this
elif not is_magician:
  print('you need magic powers')
```
