# FOR Loops

- We have work with "Conditional Logic" and "Logical Operators" to develop our code to make decisions
- Now "Loops" allow us to run lines of code over and over and over, like thousands of times or millions of times
- "Nested Loop" example at the end

- **Loops are "constructs" that enable programs (or block of codes) to execute instructions more than once, so you do not have to copy paste that code N number of times, and also can be used to iterate over sequences of items in Python**
	- "Repeat a section of code" is also called "iteration"... Or just informally, just a "loop"
	- Many objects in Python are "iterable" - meaning, we can iterate over every element in the "object" (such as every element in a List, or every character in a String)
	- We can use FOR loops to execute a block of code for every iteration (example, to print out every single letter in a String)

### Example of a simple Loop

- Example syntax of a FOR loop
- The `item_name` is a variable name that you can name however you like
```python
my_itareable = [1,2,3]  # this is a "statement (or assignment)"
for item_name in my_iterable:
	print(item_name)

>>>1
>>>2
>>>3
```

- Now another example, demonstrating how you can name your variable however you like
- Also demonstrating how the action of every iteration can be whatever you choose to execute for every element on which you iterate
```python
mylist = [1,2,3,4,5] #this is a "statement" (or assigment)
for jelly in mylist:
  print("hello Sabuza")

>>> hello Sabuza
>>> hello Sabuza
>>> hello Sabuza
>>> hello Sabuza
>>> hello Sabuza
```

- With the next example below, we first display what a "range" is and its content, to show on what we are going to "iterate against" (a Range of 10 numbers)
- Then we display an actual Loop, that iterates over each item in a list (or "range" in this case) of 10 numeric items

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

- Now we are trying to print out only even-numbers
- So, this instructions will be;
	- For every number in that List, if that number divided by 2 and remainder is equal to 0 (zero)
	- Then you can go ahead and print that number
- And then check for "odd numbers" as well
```python
mylist = [1,2,3,4,5] #this is a "statement" (or assigment)
for number in mylist:
  if number % 2 == 0: # Check for "even numbers" only
    print(number)
  else:
    print(f"Odd numner: {number}")  # Check for "odd numbers" only

>>>Odd numner: 1
>>>2
>>>Odd numner: 3
>>>4
>>>Odd numner: 5
```

- This next example starts at 0 (zero)
- then it goes "zero + 1 = 1" and gets printed out
- then goes "1 + 2 = 3" and gets printed out
- then "3 + 3 = 6"
- then "6 + 4 = 10"
- then 10 + 5 = 15
```python
for number in mylist:
	list_sum = list_sum + number
	print(list_sum)

>>>1
>>>3
>>>6
>>>10
>>>15
```

### "Nested" Loop example

- This will first complete the nested Loop (the 3 items inside the nested loop), and then go back to the initial Loop to print them together, as specified in the printing statement

- So it will go with the first item `1` in the first loop;
	- then go down to the next and last loop, and get the first item `a`
	- then go down to the last statement to print `1a` as the `print` statement says
	- so then, staying at the `1` of the first loop, it will move on to the second item in the second loop, the `b`, then print it as `1b`
	- then the third item `c` and print it as `1c`, thus completing the last loop
	- this will take you back to the first loop, and get the second item `2`
	- repeat the cycle for item `2`, and so on

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
