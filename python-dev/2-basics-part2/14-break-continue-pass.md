# Break / Continue / Pass

- When working with Loops, there are 2 other things we can use besides "break", that is "continue", and "pass"

##### Break
- It will read the line for "break" and break out of the Loop at that line
- Mainly, if a condition is met, you can break out of that Loop

##### Continue
- Once the Loop reads the line for "continue" it will go back to the beginning of the Loop
- Hence, ignoring all lines of code after the "continue", even if they are indented and belong to the block of code of the Loop
- You can kind of "skip" a condition (when it is met) and then go back to the loop

##### Pass
- This one does not do anything useful
- This will only act as a "placeholder" while you are coding
- Useful to kind of avoid syntax or error messages

# break, continue, pass

We can use <code>break</code>, <code>continue</code>, and <code>pass</code> statements in our loops to add additional functionality for various cases. The three statements are defined by:

	break: Breaks out of the current closest enclosing loop.
    continue: Goes to the top of the closest enclosing loop.
    pass: Does nothing at all.

Thinking about <code>break</code> and <code>continue</code> statements, the general format of the <code>while</code> loop looks like this:

    while test: 
        code statement
        if test: 
            break
        if test: 
            continue 
    else:

**"break"** and **"statements"** can appear anywhere inside the loop’s body, but we will usually put them further nested in conjunction with an **"if statement"** to perform an action based on some condition.

### Example of `continue` statement
```python
mystring = "Sammy"
for letter in mystring:
	if letter == 'a':
		continue
	print(letter)

>>>S
>>>m
>>>m
>>>y
```

### Example of `break` statement
```python
mystring = "Sammy"
for letter in mystring:
  if letter == 'a':
    break
  print(letter)

>>>S
```

- Another example of `break` statement
```python
# Example of "break" statement
x = 0
while x < 5:
  if x == 4:
    break
  print(x)
  x = x + 1

>>>0
>>>1
>>>2
>>>3
```
