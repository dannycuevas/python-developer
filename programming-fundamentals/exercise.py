# The Central Bank of Python gives you a loan with an interest rate of 4%. Write a Python program to read the loan **amount** from the user and calculate and print the total **interest** the customer will pay in a year. (interest = amount * (interest rate / 100)).

amount = float(input('What is the amount you want to borrow? '))
interest_rate_per_cent = 4
interest = amount * (interest_rate_per_cent / 100)
print(f'The interest you will pay in a year for Â£{amount} with an interest rate of {interest_rate_per_cent}% is Â£{interest}')

# You are asked to create a Python program that reads a temperature in **Celsius** and converts and print it to Fahrenheit. The formula is F = (C * 1.8) + 32 (where F is Fahrenheit and C is Celsius).

celsius = float(input('Please provide temperature in Celsius: '))
fahrenheit = (celsius * 1.8) + 32
print(f'Temperature in Fahrenheit: {fahrenheit}') 
