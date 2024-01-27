# EXERCISE

#First, check if the NUMBER divided by 2 has ANY decimal places

number = int(input("Enter a number of your choice:\n"))

if number % 2 == 0:
  print("This is an even number.")

#Otherwise (NUMBER cannot be divided by 2 with 0 remainder)

else:
  print("This is an odd number.")
  