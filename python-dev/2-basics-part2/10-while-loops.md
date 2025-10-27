# WHILE LOOPS

- A While Loop is different from a For Loop, in that we way "while a condition is happening; then do something"
```python
while condition:
	do action
```

- Short example, while 0 is less than 50 then do this action
```python
while 0 < 50:
	print('We got Zero')
```

- But how do we avoid executing the action infinitely? we have to "break out" of the Loop
- That is when we use the `break` statement/keyword
- So we will execute that action once, and then stop it, so it does not run for infinity

```python
while 0 < 50:
	print('We got Zero')
	break

We got Zero
```

- Then, how can we Loop specifically 50 times?
- We add a `+1` to `i` so that at some point it actually reaches to number 50, and the Loop stops
- So it will Loop from 0 up to 50 and stop as in the While statement `while i < 50:` because it reaches that number 50
- Thus, we are breaking out of the Loop by turning the Condition into False (reaching to number 50)
```python
i = 0
while i < 50:
	print(i)
	i = i + 1

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ...
46 47 48 49
```

### Using Else blocks

- We can use the `else` statement in While Loops
- In this example, we are Looping until the condition becomes False because we have reached 50, then the code says "otherwise, in this case" we are performing a last action

```python
i = 0
while i < 50:
	print(i)
	i = i + 1
else:
	print('Work is completed')

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ...
46 47 48 49
Work is completed
```
