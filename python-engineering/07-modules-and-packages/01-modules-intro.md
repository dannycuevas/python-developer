# Modules in Python

- In real life we just do not have a single file for all of our code, so how can we stay organized? 
- We will have multiple files of Python code, like a "code base" sort of speaking, for our projects

# Modules

- Can we link all of our code files together? yes we can, we call this way of organizing code as "Modules", modules are simply just the files with our code
	- by building these Modules; kind of like we built different Functions, kind of like building different classes 
	- because inside of each Module (each file), we can also have Classes, we can have Functions as well 
	- and we can also have different files, so like a "layer higher" to divide up all of our code 
	- when naming Modules we also use "snake case", for example `utility.py` or `main.py` for names (underscore and lowercase)
	- **name your modules and Functions with meaningful names, and do not use the same names as the ones already built-in with Python,** they will overwrite Python built-in Functions when being imported 

# Modules and `import` statement

- For example, we can build a `utility.py` Module, that will act like a "tool belt", containing very simple Functions that we can use all across our project 
	- we will write some code in it, like Functions for example
	- or Classes, or whatever you like

- **How are we going to use that code in `utility.py` in the rest of our code? for example, in our main file `main.py`?**
- We will just use keyword `import` followed by the name of the file where the Functions we want to use are, in this case it would be `import utility` without the `.py` extension, so just the name
	- from there, by printing out the name "utility" you would get back that file actual file path

```python
import utility

print(utility) 
```

- From there, from printing that Module, you can use check what other Functions are available in that file, like taking a quick peek while working on your main file (or from whatever you are Importing into) by using the name and dot `utility.---`

```python
import utility

print(utility.)  # <- will be displayed after the dot
```

- **While "importing", you can Import as many Modules as you want into whatever working file you are on**
	- you can repeat this as much as you like in any and all your Python files
	- so we can organize all of our code, and have all of our files in our project communicate together
	- we can "import" a Module and change its name in the process, for example `import random as cosaslocas`

```python
import utility
import utils2
import utilsss

print(utility) 
```
