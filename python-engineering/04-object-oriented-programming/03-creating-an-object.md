# Creating a new Object
  
**YouTube: Python Classes in 1 Minute!**
https://www.youtube.com/watch?v=yYALsys-P_w

- This is an example of how we would create a new Class, in this case, the "player" of a video-game
- Since this Class did not exist previously, we need to "define the class itself" in its own code within

```python
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name # attributes or properties
        self.age = age # attributes or properties
    def run(self):
        print("run") 

player1 = PlayerCharacter("Val", 5)
player2 = PlayerCharacter("Anya", 3)

print(player1.name)
print(player1.age)

>>>Val
>>>5
```

- We will also add its attributes / properties one by one, and these can be pass-in when invoking a new Object of that class
- And if we need to, we can can print them out (access the attributes) as well to find the attributes Values too, this work by using the "dot notation" `object.propertie` 

```python
player1 = PlayerCharacter("Val", 5)
player2 = PlayerCharacter("Anya", 3)

print(player1.name)
print(player1.age)

>>>Val
>>>5
```

- Here is another great example

```python
class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

warrior = Character(100, 50, 10) 
ninja = Character(80, 40, 40) 

print(f"Warrior speed: {warrior.speed}")
print(f"Ninja damage: {ninja.damage}") 
```

- The output from the above code

```python
Warrior speed: 10
Ninja damage: 40
```
