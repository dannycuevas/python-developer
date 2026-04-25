# Error Handling in Python

- **"Error Handling" allows us to let our scripts continue running even if there is an error**

### Try and Except keywords

- Let us look at the following code

```python
age = int(input("what is your age? ")) 
print(age) 

# the output:

>>>what is your age? 30
>>>30
```

- The `try:` keyword is telling Python that we want to try the following piece of code
	- everything that happens inside of the `try:` block, we are "able to handle"
- And we close it with the `except` keyword, and it tells Python that whatever is in the `try:` block;
	- if anything there errors out from there, we want something back to read instead of the regular Python all-read error messages

```python
try:
    age = int(input("what is your age? ")) 
    print(age) 
except:
    print("please enter a number")

# the output:

>>>what is your age? skaj
>>>please enter a number
```

- But how do we keep it running? we use the `while` loop
- Then we use the `else:` statement, as it would work as if working with a `if` and `elif` statements inside of a `while` loop
- The `else` will allow us to close the loop with error handling with the `break` keyword

```python
while True:
    try:
        age = int(input("what is your age? ")) 
        print(age) 
    except:
        print("please enter a number")
    else:
        print("thank you!")
        break
```

- This would be the output until we give it an actual number

```python
what is your age? qwojp
please enter a number
what is your age? alskd
please enter a number
what is your age? 30
30
thank you!
```

- Then, since using a zero/0 would be allowed, but would not make sense, we want to write the error handling as if when entering zero, it would keep the loop running
- This words because we are passing-in the `ZeroDivisionError` type error

```python
while True:
    try:
        age = int(input("what is your age? ")) 
        10/age
    except ValueError:
        print("please enter a number")
    except ZeroDivisionError:
        print("please enter a number higher than zero")
    else:
        print("thank you!")
        break
```

- The new output when using zero:

```python
what is your age? 0
please enter a number higher than zero
what is your age? qwom
please enter a number
what is your age? 30
thank you!
```
