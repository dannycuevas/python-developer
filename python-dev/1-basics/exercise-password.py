
# - Create an input, ask for a username
# - Create another input, ask for the password

# - At the end, with the input, we want to print the password information

username = input('What is your username?:\n')
password = input('What is your password?:\n')

password_length = len(password)
password_hidden = '*' * password_length


print(f'Hello {username}, your password {password_hidden} is {len(password)} letters long.')

print(f'Hello, we are testing Methods')

print('     alone here           '.strip()) # removes spaces before and after the string
print('     alone here           '.lstrip()) # removes spaces before the string
print('     alone here           '.rstrip()) # removes spaces after the string
print('Now I want some commas'.split(',')) # splits the string into a list where there are commas
print('Now I want some commas'.split()) # splits the string into a list where there are commas
