# Packages in Python

- Imagine you now also have extra folders in your Python project, as your project will get bigger and bigger over time, how can you `import` your Modules from other files in other folders that are different to your current working directory?
- Modules and Packages help us have good engineering practices, and build big projects in an organized fashion, yet still have all our files talk to each other

# Packages

- When importing modules from other folders in your project, they will not be called "modules" anymore, as they belong to other folders, they will be called "Packages"
- In other words, a Package is simply another Folder, they are a "level up", **thus a Package is a folder containing Modules**

- In order to `import` another Module from another Package into our working file, we call them by the folder directory name, and then the module name, separated by a dot, for example:

```python
import utility
import utils2
import utilsss
import shopping.shopping_cart # <-

print(shopping.shopping_cart) 
```

- Keep in mind that **in each Python package (or folder), you will have a separated file called `__init__.py`** 
	- why do we need this? because the interpreter will reach to this folder, and thanks to this file, it will know it is a an Package and not just a random folder
	- this Package file can be completely empty if you want
	- A Package inside of a Package ("nesting") will also have its own `__init__.py` file

- Example folder structure:
```python
-main.py
-utility.py
-shopping [directory]
	-shopping_cart.py
	-shopping_clients.py
	-__init__.py
-calculator.py
```

- Thus, all of this Python functionality, will allow you to keep large code projects as organized as possible
- Projects get bigger and bigger, and really good developers are able to organize code in really nice Packages and Modules that would make sense to everyone else
