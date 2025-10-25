# FOR LOOPS

- We have work with "Conditional Logic" and "Logical Operators" to develop our code to make decisions
- Now "Loops" allow us to run lines of code over and over and over, like thousands of times or millions of times

- **Loops are "constructs" that enable programs (or block of codes) to execute instructions more than once, so you do not have to copy paste that code N number of times, and also can be used to iterate over sequences of items in Python**
	- "Repeat a section of code" is also called "iteration"... Or just informally, just a "loop"

### Example of a simple Loop

- With this example, we first display what a "range" is and its content, to show on what we are going to "iterate against"
- Then we display an actual Loop, that iterates over each item in a list (or "range" in this case) of 10 items

- The `item` is a Variable that gets to be created for the Loop, and we can name it whatever we want
- **And the Variable is created in the Loop, for EACH item stored after the keyword `in`, in this case a `range(10)`** 
	- **Effectively saying "for every `item in my_range(10)` do the following action"**

- In this construct, the element `range(10)` that is acting as a "List", will be called as "Iterable"
	- An "Iterable" is something that is "able to get looped over"
```python
for item in range(10):
	print(item)

0
1
2
3
4
5
6
7
8
9

for item in range(10):
	print(f'Hello there item {item}')

Hello there item 0
Hello there item 1
Hello there item 2
Hello there item 3
Hello there item 4
Hello there item 5
Hello there item 6
Hello there item 7
Hello there item 8
Hello there item 9
```

- In the following example, we create a Loop print each character that belongs to the String
```python
for letter in 'I am Batman':
	print(letter)

I
 
a
m
 
B
a
t
m
a
n
```

- And now we will print each item in a Set
```python
for number in {1,2,3,4}:
	print(number)

1
2
3
4
```

- The following is a "nested Loop"
- This will first complete the nested Loop, and then go back to the initial Loop to print them together, as specified in the printing statement
- So it will go with A first, then B, then C
	- From there back out to the initial Loop to the 1, then 2, so on
```python
for item in (1,2,3,4,5):
	for x in ['a', 'b', 'c']:
		print(item, x)

1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
4 a
4 b
4 c
5 a
5 b
5 c
```
