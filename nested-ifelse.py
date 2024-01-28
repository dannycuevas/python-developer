# NESTED IF ELSE STATEMENTS

# First example, using a regular if statement

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height >= 120:
  print("You can ride it son!")
else:
  print("You are to short my son!")


# Second example, using a nested if else statement
  
# After we have made sure that the height is greater than or equal to 120 cm, we can use a "nested if else" statement condition that checks for their age
  
# For their age, the first condition is to check if their age is less than or equal to 18
# The secon condition, the seconde ELSE will then state that their age is greater than 18 and therefore to pay the full price
  
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height >= 120:
  print("You can ride it son!")
  age = int(input("How old are you? "))
  if age >= 18:
    print("The price is $7.")
  else:
    print("The price is $12.")
else:
  print("You are to short my son!")  

# Third example, using ELIF condition

# ELIF will represent a third condition option, and we can add as many ELIFs as we want
# In this case, ELIF represents the value of the age to be less than 12 years old
  
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height >= 120:
  print("You can ride it son!")
  age = int(input("How old are you? "))
  if age < 12:
    print("The price is $5.")  # if age is not less than 12 years old, then move on
  elif age >= 18:
    print("The price is $7.") # then, are they equal or under 18 years old, then move on
  else:
    print("The price is $12.") # so everybody else over 18 years old
else:
  print("You are to short my son!")  

