# print(list(range(10)))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#########################################

# n = 10
# i = 0

# while i < n: # while "i" is less than "n" then keep doing this:
#   print(f'Hello world by tier {i}') # print "Hello world"
#   i = i + 1 # increment "i" by 1

#########################################

# we want user to provide an answer either "yes" or "no"
# user_input = input('Please provide input (either yes or no): ')

# we want to keep the user for an "valid input" until they provide either "yes" or "no"
# of course we do not know how maney times the user will provide an invalid input 

# while user_input != 'yes' and user_input != 'no':
#   user_input = input('Please provide input (either yes or no): ')

while True:
  user_input = input('Please provide input (either yes or no): ')
  if user_input == 'yes' or user_input == 'no':
    break

# convert the answer into an F string
print(f'You said {user_input}')
