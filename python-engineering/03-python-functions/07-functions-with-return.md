# Return used in Functions

- Lets create very basic Function that sums 2 numbers, and then we print out the result of the function
```python
def sum(num1, num2):
  num1 + num2

print(sum(4,5))

>>>None
```

- As you see, the printed result of a simple sum Function was `None`
- This is because **Python Functions always have to "return" something**
	- and when they do not "return" something, with the `return` keyword, they automatically will return or print `None` as their resulting value

- So we will need to add the `return` keyword, so whenever the Function exits in a line of code, it can properly "return" or "give us" the resulting value back to us humans
	- in other words, the `return` keyword will automatically exit the Function

- Example now using the `return` keyword to actually see a visible result
```python
def sum(num1, num2):
  return num1 + num2

print(sum(10,5))

>>>15
```

### Key-points with Functions

- There is 2 really important points when working with Functions (like "best practices" for example)
	- 1- A Function should do one thing really well
	- 2- Functions should always return something back

- Also, Functions should be easy to understand
	- so "nested Functions" are really not something good, specially if you are following the 2 key-points mentioned before
