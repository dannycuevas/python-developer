# ITERABLES

- An "iterable" simply means it is an object, or a collection (like an Array for example), that can be iterated over 

- What about iterating over an object, like a Dictionary?
	- It will print out the Keys of a Dictionary, example below

```python
user = {
  "name": "Golem",
  "age": 5006,
  "can_swim": False }

for key in user:
  print(key)

name
age
can_swim
```

- Now we want to get the Key-Value pair in a Tuple-form, out of that Dictionary, when iterating over it
- We accomplish that by using the "`items.()` method"

```python
user = {
  "name": "Golem",
  "age": 5006,
  "can_swim": False }

for key in user.items():
  print(key)

('name', 'Golem')
('age', 5006)
('can_swim', False)
```

- Another "method" that we can use using `values.()`
- This will be your main option when you only want your Values printed out with the Key pairs

```python
user = {
  "name": "Golem",
  "age": 5006,
  "can_swim": False }

for key in user.values():
  print(key)

Golem
5006
False
```

- **Another useful way of collecting the items from a Dictionary, you can separate them into Key and then Value, and print them out that way too**
- Using "key" and "value" as the Variables in this example, but they can be named whatever you want, and make your code more readable

```python
user = {
  "name": "Golem",
  "age": 5006,
  "can_swim": False }

for key, value in user.items():
  print(key, value)

name Golem
age 5006
can_swim False
```
