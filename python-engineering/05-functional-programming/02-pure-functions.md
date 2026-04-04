# What is a Pure Function?

- A Pure Function has 2 rules
1. One, that given the same input, it will always return the same output
2. Two, the second point is this idea of, a Function should not produce any "side effects"
	- what are side effects? they are things that a Function does that effects the outside world
	- for example, printing something onto a screen, the screen is the "outside world" 
- Keep in mind that "Pure Functions is more of a guideline than an absolute", it is impossible to just have Pure Functions everywhere

### Example of Pure Function

- The following example of a Pure Function to demonstrate that no matter how many times we run it, it will always return the same result
- And also, how it does not touch anything in the outside world, because nothing in the outside world matters to this Function to actually work

```python
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3,4])) 

# the output:
>>>[2, 4, 6, 8]
```

- A simple example of how out Function would interact with the outside world and the screen, is changing where the empty List and the print statement are in regards to the Function actually working for us
- This is the perfect example, as we are still getting the same exact results regardless of how may times we execute the Function, but this time, there are clearly side effects

```python
new_list = []
    
def multiply_by2(li):

    for item in li:
        new_list.append(item*2)
    return print(new_list)

multiply_by2([1,2,3,4]) 

# the output:
>>>[2, 4, 6, 8]
```

- Useful Functions that we get from Python as built-in Functions, that help us allow to think in a Functional Programming Paradigm;
	- map
	- filter
	- zip
	- and reduce

### Benefits of Pure Functions

- It will be very rare to ever have a bug or an error in our code, unless we wrote something wrong all within the same Function
- But mainly, since because we do not care about the outside world, because everything that we give as an input, is always going to produce a good output, it is "going to be pure" 
- When you have pure Functions, you have less buggy code, you are able to test your code better, and it is easier to understand your code
- Overall, you have all these benefits plus not having different parts of your code touching each other, which makes your life as a developer so much easier
