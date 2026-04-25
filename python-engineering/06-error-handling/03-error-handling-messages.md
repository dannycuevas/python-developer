# Error Handling Messages

- We can also give meaningful error messages back to the screen, when using error handling
- For example, along with our error handling customized messages, we can add the actual type of error as well, thus getting customized + meaning messages, instead of long red text that is difficult to understand (using the `f String`)
- Example, in a sum Function, we will print out the message to "pass in actual numbers" plus the type of error when not passing-in numbers to the sum Function

```python
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as errmess:
        print(f"please enter numbers man {errmess}")

print(sum(1,"3")) 
```

- This would be the output when not passing numbers

```python
please enter numbers man unsupported operand type(s) for +: 'int' and 'str'
None
```

- Or we can handle different error types together, and print out whichever one was the error
- In this example, we will also check for the "division by 0" error type when passing-in the zero number

```python
def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as errmess:
        print(errmess)

print(sum(1,0)) 
```

- This would be the simple output:

```python
division by zero
None
```

### Key points with Errors

- Errors are unavoidable in programming, they are bound to happen 
- Our job in programming is to able to anticipate these errors, these bugs, these exceptions, and handle them properly in our code
