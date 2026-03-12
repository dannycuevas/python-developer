### MODULO

# In Python and many other programming languages, there is a way to check
# if a division occurs with NO Remainder
# That is through something called the MODULO
# We use the Modulo by typing a percentage % and that will give you
# the remainder after a division

#First, check if the NUMBER divided by 2 has ANY decimal places

number = int(input("Enter the number here master:\n"))

if number % 2 == 0:
  print("This is an even number.")

#Otherwise (NUMBER cannot be divided by 2 with 0 remainder)

else:
  print("This is an odd number.")
