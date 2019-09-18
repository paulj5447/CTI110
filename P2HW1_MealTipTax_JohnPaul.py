# This program calculates the tip and tax of a meal
#9/17/2019
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#John Paul

# Get the food charge
cost = float(input('Enter the food charge: '))

# Get the tip amount
tip = float(input('Enter the amount of tip as a decimal: '))

# Get the tax amount
tax = float(input('Enter the amount of tax as a decimal: '))

# Calculate the tip
tip_amount = cost * tip

# Calculate the tax
tax_amount = cost * tax

# Display calculated tip
print ('The tip is $', format(tip_amount, ',.2f'))

# Display calculated tax
print ('The tax is $', format(tax_amount, ',.2f'))

# Calculate total cost of meal
total_cost = cost + tip_amount + tax_amount

# Display total cost of meal
print ('The total is $', format(total_cost, ',.2f'))


"""for my records....notice that the total cost used the calculated tip and tax rather than the entered amount"""


            

                   
