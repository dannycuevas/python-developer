# Create a Variable that is going to ask what year were you born and store it after providing the value

birth_year = input('what year were you born?')


# Then create a program that after providing the value for the Variable, it prints out something like "your age is value"

current_year = 2025
age = int(current_year) - int(birth_year)

print(f'Your age is {age}')


# Executing the program this is how it looks

# mitrandir@vivobook:~/repos/python-developer$ python python-dev/1-basics/exercise.py 
# what year were you born?
# 1995
# Your age is 30



# instructor solution

birth_year = input('what year were you born?')

age = 2025 - int(birth_year)

print(f'your age is: {age}')
