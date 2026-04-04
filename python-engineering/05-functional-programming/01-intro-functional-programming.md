
- Let us begin with, what is a Paradigm?, it is a way to;
	- to think about our code
	- and a way to organize our code 

> # History of programming languages
> https://en.wikipedia.org/wiki/History_of_programming_languages

- Functional Programming is all about "separation of concerns" (something that OOP does as well), it is all about packaging our code into separate chunks so that everything is well organized in each part of our code (and each part is organized in a way that makes sense, based on functionality)

- **So when we say "separation of concerns", we mean, that each part concerns itself with one thing that it is good at**
	- example, in OOP, we had "classes" to divide up attributes and methods
	- **but, in Functional Programming they also separate Data and Functions (this paradigm is also referred to as "Pure Functions")**
	- instead of combining methods and attributes, like in OOP, we separate them up, because they are 2 separate things 
	- so, we are not going to combine both Data and Functions as one single piece in an Object, like in OOP

- Now, **there is no correct definition for what is and what is not "functional", but generally, functional languages have an emphasis on simplicity, where Data and Functions are concerned** 
	- because in most functional programming paradigms, we do not have this idea of classes and objects 
	- instead, **Functions operate in well-defined Data Structures (like Lists and Dictionaries), rather than belonging that Data Structure to an Object**

- The end goal of a Functional Programming Paradigm is the same as Object Oriented Programming, it is the idea of;
	- making our code clean and understandable
	- easy to Extend 
	- easy to maintain 
	- memory efficient
	- keeping out code DRY (we are not repeating ourselves) 

# What “Functional Programming” Means (in simple terms)

Functional programming is a style where you:
- treat functions like data    
- use functions inside other functions    
- avoid changing variables when possible    
- process collections (lists, data) with small functions    

In Python, this usually means things like:
- `map()`    
- `filter()`    
- `lambda`    
- list comprehensions    
- `sorted()` with functions

# The FP Tools DevOps Engineers Actually Use

These are the ones you may see in real scripts.

|Tool|Used Often?|Purpose|
|---|---|---|
|`lambda`|sometimes|small one-line functions|
|`map()`|rarely|apply function to list|
|`filter()`|rarely|filter items in list|
|`sorted()` with key|common|sorting data|
|list comprehensions|**very common**|transforming lists|
