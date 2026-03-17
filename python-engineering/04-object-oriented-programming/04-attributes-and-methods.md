# Functions Attributes and Methods

**When to use what? - And "Class Methods"**
https://www.makeuseof.com/tag/python-instance-static-class-methods/

- Object Oriented Programming allows us to create Objects that have their own Methods and Attributes
	- OOP allows us to write code that is repeatable, well organized, and also memory efficient 

- This is a great way to add "functionality to a language" and try to mimic the real world
	- this is thinking less procedural and thinking more in terms of functionality 
	- grouping Data like Attributes, together with Methods, to create a Class that is like somehow able to mimic something from the real world 

# Attributes and `self`

- Attributes are pieces of Data that are dynamic
- Meaning, when we instantiate a new Object, they are going to be unique to that specific Object, like "name" and "age" 
- And we have to use the `self` keyword, to make sure it was dynamic
	- all Methods in a Class receive the first parameter as `self` so that we can call them and use them
	- and so `self` will be the new Object, and the line means: "Store the name and age (the variables) inside this Object"
	- the `self` variable is supplied automatically when using the `__init__` method, and it is always places as the first variable

```python
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name # attributes or properties
        self.age = age # attributes or properties
    def run(self):
        print("run") 
```

- However, **there is another thing called the "Class Object attribute"**
- This will be on the same line as the Methods
- And this one is different, because this one is not Dynamic, this one will be Static

```python
class PlayerCharacter:
	# -> Class Object Attribute <-
	membership = True
	
    def __init__(self, name, age):
        self.name = name # attributes or properties
        self.age = age # attributes or properties
    def run(self):
        print("run") 
```

- Thus, this attribute will exist in all following Objects created from this blueprint, it will not change across instances 

- We can use this static attribute to tell our Class that for every new Object, it will only have attributes if the Class Object Attribute is True

- Example
```python
class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership): # only if True, then:
          self.name = name # attributes or properties
          self.age = age # attributes or properties
    def shout(self):
        print(f"my name is {self.name}") 

player1 = PlayerCharacter("Val", 5)
player2 = PlayerCharacter("Anya", 3)

print(player1.shout())
print(player2.shout())  
```

- The output
```python
my name is Val
None
my name is Anya
None
```

- The "Class Object attribute" is right at the definition of the Class, and will not change across instances
- An "Object Attribute" is something that is Dynamic, and is unique in every single Object (not the Class / blueprint)
	- it is defined in our "constructor" function, the `__init__()` function 

- Thus, the way we access them is different, for the Class object Attribute, we can call it by its actual Class name, like "membership"

```python
class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership): # only if True, then:
```

- To access an Object Attribute anywhere inside of our Class, we have to use the `self.` keyword followed by the attribute

```python
def __init__(self, name, age):
        if (PlayerCharacter.membership): # only if True, then:
          self.name = name # attributes or properties
          self.age = age # attributes or properties
    def shout(self):
        print(f"my name is {self.name}") 
```
