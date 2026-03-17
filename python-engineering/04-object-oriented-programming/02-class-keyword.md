
# What is the `class` Keyword

- In Python, we can create our own Data Type, our own "Class", by using the `class` keyword and name it whatever you want
- The naming convention will change, we will "capitalize" our class names, and every new word, will be a capital letter 

- For example:

```python
class BigObject:
    pass # this is where the code goes
```

- And now, if we create an object out of that class, we will see that the name given to that class will be the "class" Data Type
- Just ignore the `__main__.` text

```python
class BigObject:
    pass

obj1 = BigObject()

print(type(obj1)) 

# the output:
<class '__main__.BigObject'>
```

### What is the "Class"?

- The "class" then would be known as the "blueprint" of what we want to be creating, like what Objects we want to be creating, with our code
	- it will help us define what are the basic attributes, and the properties that our class will have
	- also, will help us define what are some basic "methods or actions" that our class can receive from us

### What are the "objects"?

- Then, from that blueprint, we are able to create different objects, over and over, using the "blueprint" as the building block for whatever many objects we want
- Thus, we can say that "the class can be instantiated", or in other words, the action of creating different "instances" as we like using the "blueprints"
	- and what are these "instances"?, they will be the actual objects created out of the "blueprints"
	- so, saying "I just instantiated a class", means, "I just created a new instance / object"


# Key takeaways

**How does "creating a new class an a new object will look like"?**
- A newly created class, and all of its code within, will be "stored in memory"
- But every time we create an Object, we do not have to rewrite the entire code or anything like that 
- Python will go in memory where the class is and just run that code, allowing us to keep our code "dry" ("do not repeat yourself")

### Quick Summary Table

|Concept|Meaning|
|---|---|
|`class`|blueprint|
|object|instance created from class|
|`__init__`|setup function for the object|
|`self`|the current object|
