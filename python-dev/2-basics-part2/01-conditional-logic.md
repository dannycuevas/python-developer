# CONDITIONAL LOGIC

- "Conditional logic" will allow us to apply "control flow"
- "Control flow" basically allows us to use "logic to execute code only when we want to"
- To "control this flow of logic" we use these 3 keywords:
	- `if`
	- `else`
	- `elif`
	- the "control flow syntax" makes use of colons and indentation (the white spaces)

- Then, **the `if` statement is a "conditional operation"**
- In Python we use the `if` keyword to say:
	- IF some conditions exists (like True or False) then "perform this action"
	- IF that condition does not exist, then "perform this other action"

- Basic "if statement" syntax example:
	- "the condition" is usually some sort of "comparison operation" 
```python
if some-condition-met:
	# then execute this code
```

# IF statement

- Example, checking if a person "is old enough" and "is licensed" then that person can drive
- So if the condition is True (it is by default), then run all the code inside that indented block of code
```python
is_old = True
is_licensed = True

if is_old:
	print('you are old enough to drive')

>>>you are old enough to drive
```


# ELSE statement

- Then, to make the code "perform a different action when the condition is not met" (when it is not True), we then add `else` 
- In this example, the condition is now False, so it will print the result of the `else` statement
```python
is_old = False
is_licensed = True

if is_old:
	print('you are old enough to drive')
else:
	print('no check here')

>>>no check here
```
- `else` will act as the last "catch all" conditional, it will execute when ALL other conditions have failed


# ELIF statement

- So `elif` will allow you to check multiple conditions before reaching the very last one with `else`
	- If any of the conditions are met, then the code will execute the last line of code under `else` statement
- Example syntax:
```python
if some-condition-met:
	# then execute this code
elif some-other-condition-met:
	# do something different
else:
	# do something else
```

- And it will also allow you to have multiple or as many `elif` statements as you want
- Example 1:
```python
# location
loc = 'Bank'

if loc == 'Auto Shop':
	print("Cars are cool")
elif loc == 'Bank':
	print("Money is cool")
elif loc == 'Store':
	print("Welcome to the store")
else:
	print("I do not know much")

>>>Money is cool
```

- Example 2:
```python
is_old = False
is_licensed = True

if is_old:
	print('you are old enough to drive')
elif is_licensed:
	print('you have a license to drive')
else:
	print('no check here')

>>>you have a license to drive
```

### Complete example

- This is a more realistic example of how code will look like
```python
if case1:
	perform action 1
elif case2:
	perform action 2
else:
	perform action 3
```
