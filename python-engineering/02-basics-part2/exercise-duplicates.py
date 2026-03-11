# We will check for duplicates in a List, print out the duplicated values

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# First we create an empty Variable called "duplicates", which will be an empty List for now
#   and we will populate with the duplicated values

# Then Loop over the List, and use the "count()" function, saying that if it is greater than 1 then there is a duplicate
#   "count()" allows us to count "how many times an item in a List exists"
#   and we are going to add that duplicate to the duplicates=[] empty List
#   so it will get that duplicated Value as "value" and .append() that Value to the duplicates=[] List

# Then, since we do not need to print out all the duplicated Values, we use another IF statement 
#   that says "if that value do not already exist, then execute to append it to "duplicates" Variable"
#   meaning, if that Value already exist in that Variable, it will not be appended 

duplicates = []
for value in some_list: # loop for everuy item within the List
  if some_list.count(value) > 1: # counting how many times that "value" happens in the List
    if value not in duplicates: # check if that value is not in "duplicates" List already, so if not then:
      duplicates.append(value) # so if not already in duplicates List, then append that value

print(duplicates)                                                                              

# At the end, this will only print out: ['b', 'n']
# And will not print out copies of all the times the Values are duplicated 
