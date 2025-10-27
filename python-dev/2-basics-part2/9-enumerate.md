# ENUMERATE function

- The `enumerate.()` function will return an enumerate object, and we have to pass to it a iterable, meaning, something that enumerate can iterate over

- What it is going to give us is, it is going to take an iterable object, and gives you in "index counter" and the item of that index

- In this example we print `i` and `character` 
```python
for i,char in enumerate('Hellooooo'):
	print(i, char)

0 H
1 e
2 l
3 l
4 o
5 o
6 o
7 o
8 o
```

- **The difference here is that, because we are using "enumerate" with `i` in the Loop, as an "index counter", we are printing out the iterable of the Loop along with their index counter together**

### Example

- We want to be told what the index of number 50 is, by using "enumerate"
- It will come out of a Range, that is converted into a List
- So, we want to only print out the index of a specific number, in this case number 50

```python
for i,char in enumerate(list(range(100))):
	if char == 50:
		print(f'index of 50 is: {i}')

index of 50 is: 50
```
