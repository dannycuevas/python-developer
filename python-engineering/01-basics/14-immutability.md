# IMMUTABILITY

- This is an important term in programming
- Being immutable means that it cannot be changed

- Example of this concept is a "String", once it is created and a Value has been assigned to that Variable, it cannot be changed
- This is unless the string is recreated with a new assigned Value

- What will happen is that Python will remove that Value (which is stored in memory), and then assigned the new Value 

- In this example, the original `pinkcube` Variable will no longer exist, and will only exist in the final version of the Variable
```python
>>> pinkcube = '012345'
>>> pinkcube = pinkcube + '6'
>>> print(pinkcube)
0123456
```
