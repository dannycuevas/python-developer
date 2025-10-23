# TERNARY OPERATOR

- Ternary Operator is another way of doing Conditional Logic, like a shortcut of the regular `if-else` statements, for you to make your code cleaner

- **A ternary operator is a Conditional Expression; such is an operation that evaluates to something, based on the condition being True or not**

- Example, "if the condition" (the one in the middle) is True, then execute what is on the left side of the expression
	- But "if not True", then execute what is on the right side of the expression
```python
condition_if_true if condition else contidion_if_false
```

### Example

- Now we will do an example of an object, such as a user, that can message you only if that person is listed as your friend

- The condition is True
- The user "can message you", if the condition is True
- If the user is not your friend then "it is not allowed"
- Lastly, print out the final result
```python
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

>>>message is allowed
```
