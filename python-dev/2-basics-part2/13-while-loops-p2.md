
### While Loops / Comparing Loops

- While Loops tend to be more flexible than For Loops
	- This is mainly because they can Loop many more times than a For Loop
	- It all depends how you manage your "conditional statements" in your Loops
	- One downside is that we have to create a Variable, and then remember to increment that Variable so we do not execute a While Loop infinitely 

- In the other hand, For Loops are simpler, thus the code for For Loops look and read very well
	- Mainly because it is already explicit how many times we are looping over an object

### While Loop with an Input

- One interesting way to use While Loops is to run the Loop with an Input
- Meaning, ask for an Input, and once the Input has executed, you break out of the Loop

```python
while True:
	input('Say something here: ')
	break

Say Something here: hell there machine
```

- But then, we can While Loop asking for an Input, but do not Break out of the loop until the right Input has been entered
- This will work using Conditional Logic
- We collect the Input as a Variable, and use an `if` statement, that until that "conditional logic" has been met, it will then execute the `break` out of the Loop

```python
while True:
	response = input('Say something here: ')
	if (response == 'bye'):
		break
```
