
# Ask the teacher to provide a test mark  
# The input goes into the Function "int()" for integer conversion
# The input is then stored in the variable "test_mark"

mark = int(input('Provide test mark: '))

# Now we want our program to print, for example, if A is mark over 7
# The colon (:) defines the end of the condition - IF statement

if mark > 7:
  print('Grade A - Well done!')
  if mark > 9:
    print('You have achieved a distinction!')

print('End of program for marks. Good luck.')
