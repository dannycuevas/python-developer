print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". \n').lower()

# The "choice2" input line has to run when the choice1 is equal to "left", otherwise we will get an indentation error. So indent the line to show that that line is part of "if choice1" statement and will only be excuted if "if choice1" is True.

# And then we get to check the "choice2" line.

if choice1 == "left":
  # Left will continue the game.
  choice2 = input('You\'ve come to the lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    # Wait will continue the game.
    choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()
    # We are adding 4 possible things that could happen. But 3 are our 3 main paths, so they are given their own dialogs. The fourth one ("else"), is just a safe mechanism for cheaters, just in case.
    if choice3 == "red":
      print("It is a room full of fire. You screamed to death. Game over!")
    elif choice3 == "yellow":
      print("You have just found the treasure. You are the promised prince. YOU WIN.")
    elif choice3 == "blue":
      print("You entered a room full of witches, they burned you. Game over!")
    else:
      print("That option does not exist, you cheater. Game over!")
  else:
    print("You just got attack by an evil shark!. Game over!")
else:
  print("You fell into a hole!.Game over!")
