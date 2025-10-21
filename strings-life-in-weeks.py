# Create a program using maths and f-Strings that tells us how many weeks we have left,
# if we live until 90 years old.

### Solution
# -First we need to calculate how many years they have left
# -Remeber the input comes a String data type, and we need to convert it to an integer
# (whole number), to be able to do a mathematical operation

age = input()
15

### Formula

years = 90 - int(age)

# -There are 52 weeks in a year
# -So we can be able to multiple the number of years left by 52, to get the number of 
# weeks left

weeks = years * 52
print(f"You have {weeks} weeks left.")
