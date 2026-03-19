
Here is the 5-line mental model that makes OOP (classes, objects, `self`, and `__init__`) suddenly make sense for beginners

# The 5-Line Mental Model
This is literally 90% of OOP

| Line | Concept        | Simple Meaning                                    |
| ---- | -------------- | ------------------------------------------------- |
| 1    | **Class**      | A blueprint for something                         |
| 2    | **Object**     | A real thing created from the blueprint           |
| 3    | **`__init__`** | The setup that happens when the object is created |
| 4    | **`self`**     | The current object being created                  |
| 5    | **Methods**    | Actions the object can perform                    |

- Example Using This Model
```python
class Server:

    def __init__(self, name):
        self.name = name

    def start(self):
        print("Starting", self.name)


vm1 = Server("web01")
vm1.start()
```

- The Output
```python
Starting web01
```

- **Step-by-Step What Happens:**

| Step | Python Action                                 |
| ---- | --------------------------------------------- |
| 1    | Python reads the **class blueprint**          |
| 2    | `vm1 = Server("web01")` creates an **object** |
| 3    | Python automatically runs `__init__`          |
| 4    | `"web01"` gets stored as `self.name`          |
| 5    | `vm1.start()` runs the method                 |

# Visualizing It
Think of it like a **factory**

```python
Blueprint (class)
       |
       v
Factory builds object
       |
       v
__init__ installs parts
       |
       v
Object ready to use
```

- Following the same example:
```python
Server class
      |
      v
Server("web01")
      |
      v
__init__ runs
      |
      v
vm1.name = "web01"
```

# Real DevOps Example
Imagine modeling cloud VMs

```python
class VM:

    def __init__(self, name, region):
        self.name = name
        self.region = region

    def start(self):
        print("Starting VM", self.name)


vm = VM("web01", "eastus")
vm.start()
```

- The output:
```
Starting VM web01
```
