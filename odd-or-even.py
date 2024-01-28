# EXERCISE

# First step, create variable to store a number and then convert it to an integer, so it can later be used as a variable and be divided by 2

number = int(input("Enter a number of your choice:\n"))

# We will divide the number by 2 and check if the remainder is 0. And this is equivalent to saying; if the number divided by 2 has no decimal places, then this is an even number.

if number % 2 == 0:
  print("This is an even number.")

# Otherwise (NUMBER cannot be divided by 2 with 0 remainder)

else:
  print("This is an odd number.")
  