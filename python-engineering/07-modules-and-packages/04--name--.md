# __name__

- When we run a Python file, usually we are running just the current working file, and when we click "run", the interpreter goes line by line in our file from top to bottom 
- So, if you are importing Functions from other Modules or Packages, "importing" are usually the first lines in your current working file, so they are the first lines the interpreter executes, for example:

```python
from utility import multiply, divide
from shopping.more_shopping.shopping_cart import buy

print(buy("apple"))  
print(divide(5, 2))
```

- So if each of those Modules and Packages have the `print(__name__)` Function at the beginning of their respective Files, then your "running" in your console will print out the names of those Modules or Packages as it is also "importing" their Functions
- Example of the `utility.py` Module that is being imported to our main working file:

```python
print(__name__)
def multiply(num1, num2):
	return num1*num2

def divide(num1, num2):
	return num1/num2
```

- Working in your main file when you `run` and `import` something in Python;
	- reads the first line where your are "importing" something to your current working file
	- then it finds the Module by folder structure
	- it then runs the code in the Module as well, so it adds the Module's code to memory
	- and then it "runs" to the second line in your current working file where you started your `run` command
	- and goes on executing line by line
	- hence, why we should always add the first line of code of `print(__name__)` to each Module or Package

# `__main__` Name

- **When "running", when you run the `run` command, your current working file will become `__main__` automatically, as Python is understanding that `__main__` is just where you have executed the `run` command**
- This will always apply regardless of your file name, so whether it is called `main.py` or `supersaiyan.py`, once you execute the `run` command, if you print it, it will become `__main__` 
- Thus, the `__main__` name is given specifically, only, to the file we are running 

### Example `__main__`

- We can make sure to only run code from the main file, and the main file is where we are running `run` from, and more than likely, is where where are "importing" Modules and Packages into as well, to execute some code
	- just add the following block of code (down below) in the main file where we are executing the `run` command from
	- note, that our "running file" must not be named like a "Module" would be in our project
- **This block code will only work when we directly run `run` the current working file that contains this block of code**
	- **meaning, anytime we `run` a Python file, it "becomes the main file" automatically, and so the condition `if name == main` will be met and true**
	- if you are "importing" a Module into your working file that also contains this block of code, it will not work as the "main" file, so this block of code will only ever work in the "main" file (whatever we are running `run` from)
	- think of this process as "consuming vs running" 
- This is a common structure as projects grow bigger and bigger, and maybe we have code around that we do not really want to always `run` other than the one from `__main__` file

```python
# make sure this is the "main" file
print(__name__)

# execute this code only if this is "main"
if __name__ == '__main__':
	print("please run this")
```

- And so, then we can take it one step further
- We can also wrap around the main file code, to make sure that we only `run` / execute that code if we are only running the "main" or current working file

```python
from utility import multiply, divide
from shopping.more_shopping.shopping_cart import buy

if __name__ == '__main__':
	print(buy("apple"))  
	print(divide(5, 2))
	print(multiply(5, 2))
	
	print("please run this")
```

### "Classes" with `__main__`

- Going back to "classes" for a bit
- Whenever you have instantiated a Class, and printed out its `type()`, and you see the `__main__` there, it just means that this instance of the Class was created in the "main file" that was just `run` commanded
- Example with a simple Class that does not have anything, but we just use it as example:

```python
class Student():
    pass

st1 = Student()

print(type(st1)) 

# the output
<class '__main__.Student'>
```

- If you are printing out this instance of the Class, from another file that is actually "importing" the Class from another file, then the Object will take this working file name instead of the "main file" where it was originally created
- Example, running the `run` command from another file named `utility.py`, importing the Module that contains the original Class, will get us something different

```python
import utility

print(type(utility.st1))

#the output
<class 'utility.Student'>
```
