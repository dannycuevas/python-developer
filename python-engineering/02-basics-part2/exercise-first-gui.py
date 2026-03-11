# Loop through this List of Lists, and everytime you encounter a number zero, display an empty space
# and evertime you encounter a 1, display an *

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# What do we want to do?
#   1- we want to iterate over picture
#   2- then iterate again inside the nested List one yb one
#   if 0 -> print ' ' 
#   if 1 -> print *

# This will be a nested FOR Loop
# And because this will convert into an image, we want to use the end() function
# So after looping an entire "row" (one actual List), then we can print() a new line below

for row in picture:
  for pixel in row:
    if (pixel == 1):
      print('*', end='')
    else:
      print(' ', end='')  
  print('')
