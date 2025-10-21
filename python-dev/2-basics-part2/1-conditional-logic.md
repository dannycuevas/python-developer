# CONDITIONAL LOGIC

- The `if` statement is a "conditional operation"
- In Python we use the `if` keyword to say:
	- IF some conditions exists (like True or False) then "perform this action"
	- IF that condition does not exist, then "perform this other action"


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

- Then, to make the code perform a different action when the condition is not met, we use `else` 
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

- `else` will act as the last "catch all" conditional, it will execute when ALL other conditions have failed
- So `elif` will allow you to add more conditional statements before reaching the very last one with `else`
	- And it will also allow you to have multiple or as many `elif` statements as you want
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
