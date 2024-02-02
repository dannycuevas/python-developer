# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# 1-Take both people's names and check for the number of times the letters in the word TRUE occurs.

# 2-Then check for the number of times the letters in the word LOVE occurs.

# 3-Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? \n") # What is your name?
name2 = input("What is her name? \n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# First combine the names together so we have a single string to check
combined_names = name1 + name2
# Next step, take all of the characters and make sure the casing is the same as what we are going to check it against
lower_names = combined_names.lower()

# Next we check how many times the letter "true" occurs in both the names, so we will check it agains the combined lower case names
# Then we use the count method to see how many times the letters occurs in the combined name, and we add those numbers all up together in order to get a hold of our "first_digit" for our love calculator
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

# And we do the same thing for the second_digit.
# We count how many times the letters "love" occurs in the combined lowercase names, and we add all of those occurrences up to get our "second_digit"
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# Once we have got both digits, then we can combine them together
# And the way the calculator works, we need to add the first_digit and the second_digit together to create a 2-digit number
# So we will turn our digits into strings, so that we "combine them", rather than add them up, using the STRING method, and we use the PLUS sign in order to concatenate them together so that they occur one after the other as if it was text

"score = str(first_digit) + str(second_digit)"

# Final step is to check the score againts the conditions that we set out, so we can give people an interpretation of their score
# So we will turn our combine love score into an integer

score = int(str(first_digit) + str(second_digit))

# All that is left to do is to write an if-elif-else statement in order to check agains the 3 conditions
# And if all of the first conditions are not true, then ELSE, we just print out their score in the third statement
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
  