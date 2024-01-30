# MULTIPLE IF STATEMENTS

# The most important part of the code is the indentation, as it declares how the IF statements will be run.

# For example, the print statement for the BILL will run "after" the wants_photo statement has been run.

# For the billing, a "dedicated" BILL variable is defined depending on the AGE input/variable. And since only 1 bill will be executed depending on the AGE, then that bill +3 is what is going to be printed at the end.

# Because the if-elif-else statement is only ever going to be TRUE ofr the AGE varible.
# And the "wants_photo" statement is completely separate from the if-elif-else statement, but still TRUE for the AGE and HEIGHT variables, therefore printing the final bill price.


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
