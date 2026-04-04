# The __ init __ Function

- The `__init__` is a "constructor function", with double dashes at the beginning and at the end
	- it will "get called" every time we instantiate a new Object (out of the blueprint) 
	- and provides us with safeguards for control when instantiating new Objects 

#### Important Beginner Tip
- You could also argue that `__init__` is **not the constructor** exactly — it’s the **initializer**
- But, for beginners, it's fine to think of it as the **object setup function** or the constructor
- In other words, this method initializes the Object, and also handles the inputs

# The Simple Idea

> **`__init__` is a function that runs automatically when you create an object from a class**
> Meaning; `__init__` automatically sets up an object when it is created

- Think of it as a **setup function**.
- It prepares the object with the information it needs.

# Real-World Analogy

- Imagine a **car factory**, and see how the concepts compare to each other, from real life to Python code

|Concept|Real World|Python|
|---|---|---|
|Blueprint|Car design|Class|
|Car created|A real car|Object|
|Setup when built|Add engine, color|`__init__` function|

- So when the car is built, the factory **initializes it** with its properties.
- That’s why it’s called **initialize** → `__init__`.

### Example Without `__init__`

- Here we created a new Object, but has no data inside it
```python
class Server:
    pass

vm = Server()
```

### Example With `__init__`

- Here we use the `__init__` and we are able to add attributes and call them too
```python
class Server:

    def __init__(self, name):
        self.name = name

vm = Server("web01")

print(vm.name)

# Output:

>>>web01
```

- **What Happens Step-by-Step:**

| Step | What Python Does                        |
| ---- | --------------------------------------- |
| 1    | You create the object                   |
| 2    | Python calls `__init__` automatically   |
| 3    | The object gets initialized with values |

### Visual explanation

```python
Server class
      |
      v
vm = Server("web01")
      |
      v
__init__ runs automatically
      |
      v
vm.name = "web01"
```

- Example of what DevOps Engineers Might Write
```python
class VM:

    def __init__(self, name, region):
        self.name = name
        self.region = region

vm1 = VM("web01", "eastus")

print(vm1.name)
print(vm1.region)
```

- Output:

```python
web01
eastus
```
