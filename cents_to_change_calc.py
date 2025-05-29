cents = int(input("How many cents are there to convert to dollar bills and change? "))
original_cents = cents 
dollars = 0 
quarters = 0 
dimes = 0 
nickels = 0 
pennies = 0 

if(cents >= 100):
    dollars = cents // 100
    cents = cents % 100 
if(cents >= 25):
    quarters = cents // 25
    cents = cents % 25
if(cents >= 10):
    dimes = cents // 10 
    cents = cents % 10 
if(cents >= 5):
    nickels = cents // 5 
    cents = cents % 5 
if(cents >= 1):
    pennies = cents
    cents = 0

print(f"{original_cents} cents is {dollars} dollar{'s' if (dollars != 1) else ''}, {quarters} quarter{'s' if (quarters != 1) else ''}, {dimes} dime{'s' if (dimes != 1) else ''}, {nickels} nickel{'s' if (nickels != 1) else ''} and {pennies} penn{'ies' if (pennies != 1) else 'y'}.")
