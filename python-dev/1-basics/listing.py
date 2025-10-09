# my_book = {
#   'basket': [1,2,3],
#   'color': 'yellow',
#   'greet': 'hello'
# }

# print('basket' in my_book)

###########################################################################
# def sum_of_change(a, b, c):  # -> Parameters: a and b
#     moneda = a - b - c           # -> Task: Addition
#     return moneda            # -> Output: Sum of a and b

# ### -> Calling the function with inputs 5 and 7
# result = sum_of_change(200, 13, 52)

# print(result)  # Output:
###########################################################################

# using Try- except 
try:
	# Attempting to divide 10 by 0
	result = 10 / 0
except ZeroDivisionError:
	# Handling the ZeroDivisionError and printing an error message
	print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")
