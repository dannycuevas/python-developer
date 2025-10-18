Here’s a compact, beginner-friendly cheat sheet of **common Python built-in functions**.  
(Examples show a tiny expression ➜ its result.)

| > Function    | > What it does                            | > Tiny example ➜ Output                             |
| ------------- | ----------------------------------------- | --------------------------------------------------- |
| `print()`     | Writes text/values to the screen          | `print("Hi")` ➜ `Hi`                                |
| `input()`     | Reads a line from the keyboard (as `str`) | `name = input()`                                    |
| `len()`       | Number of items/characters                | `len("cat")` ➜ `3`                                  |
| `type()`      | Shows the object’s type                   | `type(3.5)` ➜ `<class 'float'>`                     |
| `int()`       | Convert to integer                        | `int("7")` ➜ `7`                                    |
| `float()`     | Convert to float                          | `float("3.14")` ➜ `3.14`                            |
| `str()`       | Convert to string                         | `str(42)` ➜ `"42"`                                  |
| `bool()`      | Convert to boolean                        | `bool(0)` ➜ `False`                                 |
| `list()`      | Make a list                               | `list("abc")` ➜ `['a','b','c']`                     |
| `tuple()`     | Make a tuple                              | `tuple([1,2])` ➜ `(1, 2)`                           |
| `set()`       | Make a set (unique items)                 | `set([1,1,2])` ➜ `{1, 2}`                           |
| `dict()`      | Make a dictionary                         | `dict(a=1, b=2)` ➜ `{'a':1,'b':2}`                  |
| `range()`     | Integer sequence (often for loops)        | `list(range(3))` ➜ `[0,1,2]`                        |
| `sum()`       | Sum numbers in an iterable                | `sum([1,2,3])` ➜ `6`                                |
| `min()`       | Smallest item                             | `min(5, 2, 9)` ➜ `2`                                |
| `max()`       | Largest item                              | `max([9, 3, 7])` ➜ `9`                              |
| `sorted()`    | New sorted list                           | `sorted([3,1,2])` ➜ `[1,2,3]`                       |
| `reversed()`  | Iterator reversed                         | `list(reversed([1,2,3]))` ➜ `[3,2,1]`               |
| `enumerate()` | Pairs index + item                        | `list(enumerate(['a','b']))` ➜ `[(0,'a'),(1,'b')]`  |
| `zip()`       | Pair items from iterables                 | `list(zip([1,2], ['a','b']))` ➜ `[(1,'a'),(2,'b')]` |
| `any()`       | `True` if any item is truthy              | `any([0, "", 5])` ➜ `True`                          |
| `all()`       | `True` if all items are truthy            | `all([1, "x", True])` ➜ `True`                      |
| `abs()`       | Absolute value                            | `abs(-7)` ➜ `7`                                     |
| `round()`     | Round number                              | `round(3.1416, 2)` ➜ `3.14`                         |
| `pow()`       | Power (like `**`)                         | `pow(2, 3)` ➜ `8`                                   |
| `divmod()`    | Returns `(quotient, remainder)`           | `divmod(7, 3)` ➜ `(2, 1)`                           |
| `map()`       | Apply function to items                   | `list(map(str, [1,2]))` ➜ `['1','2']`               |
| `filter()`    | Keep items where function is `True`       | `list(filter(bool, [0,1,2]))` ➜ `[1,2]`             |
| `next()`      | Get next item from iterator               | `next(iter([10,20]))` ➜ `10`                        |
| `open()`      | Open a file (returns file object)         | `f = open("file.txt")`                              |
| `help()`      | Quick docs in the REPL                    | `help(len)`                                         |
