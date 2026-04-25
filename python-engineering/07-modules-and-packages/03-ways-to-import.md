# Different ways to "import"

- When importing a nested Package, one that is inside an actual Package, we will call all the folders names, and Path, to import it, pretty simple, like this example:

```python
import utility
import utils2
import shopping.shopping_cart
import shopping.more_shopping.shopping_cart

print(shopping.more_shopping.shopping_cart.buy("apple")) 
```

# `from` Keyword

- A much cleaner way to Import, is to use the `from` keyword
	- it will allows us to just name the folder(s), and then select what specific Function to bring over an "import it"
	- we use `from` to search the folder structure, and then `import` to select the Function
	- and then run `print()` for that specific Function as normal, as if it was part of your current working file

```python
import utility
import utils2
import shopping.shopping_cart
from shopping.more_shopping.shopping_cart import buy

print(buy("apple"))  
```

- When "importing" multiple Functions, just add a comma between them when calling them, example below

```python
from utility import multiply, divide
from shopping.more_shopping.shopping_cart import buy

print(buy("apple"))  
print(divide(5, 2))
print(multiply(5, 2))
```

### Key-points

- Importing with `from` would be the better option in large projects, as it helps with avoid naming collisions
- And overall, it is usually more readable and organized to just use `from` when importing 
- When importing, pay attention to names not overwriting Python built-in features, like Functions
