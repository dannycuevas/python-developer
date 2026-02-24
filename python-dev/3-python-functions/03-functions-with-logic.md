# Functions with Logic

- Now that we understand Data Types like Strings, Integers, List, etc, and we also know "conditional statements", For and While loops, we can being adding "logic" statements to our Functions

- In this example, we will create a Function that will iterate inside a List and check for ANY even numbers

```python
# return True if any number is even inside of a List
# the parameter we are passing-in is assumed to be the List
def even_list(num_list):
  for number in num_list:   # check FOR every item inside my object (this List)
    if number % 2 == 0:   # if any item mod 2 is equal to zero
      return True   # then return True
    else:   # if none found, then
      pass   # keyword "pass", so do not do anything
```

```python
# now we pass-in a List with even numbers to make sure it works
even_list([2,4,5])

>>>True
```

>NOTE
>- Listed much more examples in Jupyter notebook 4

- Another example of a Function:
	- Define a function called `myfunc` that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase
	- Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation
	- The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string
```python
def myfunc(x):
  out = []
  for item in range(len(x)):
    if item % 2 == 0:
      out.append(x[item].lower())
    else:
      out.append(x[item].upper()) 
  return ''.join(out)     
```

- Execute that Function passing-in a String
```python
myfunc("superman")

>>>'sUpErMaN'
```

- Example "Permission checker" Function
**Problem**  
Create a function called `has_access` that:
- Takes one parameter: `role`    
- If role is `"admin"` → return `"Access granted"`    
- Otherwise → return `"Access denied"`
Then:
- Call the function    
- Store the result in a variable    
- Print the result
**Hints 💡**
- Use `return`, not `print`, inside the function    
- Print the result **after** calling the function
```python
def has_access(role):
    if role == "admin":
        return "Access granted"
    else:
        return "Access denied"

# Function runs
# "return" value will be stored in "result" Variable
result = has_access("admin")
print(result)
```

#### 🧠 Super important rule (write this in your brain 🧠✍️)

❌ Never assign the result of `print()` to a variable  
✅ Assign the result of `return` to a variable

#### 🔑 One-sentence takeaway
`print` talks to humans
`return` talks to your program
