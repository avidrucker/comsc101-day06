# SDM: this program will take in
# a user inputted positive integer,
# and it will respond back with
# "This number is even" or
# "This number is odd"

# get user input and assign it to a variable
num = int(input("Please enter a positive number: "))

# we check, is num evenly divisble by 2
if(num % 2 == 0):
    # if it is divisible by 2, we print 
    print("This number is even")
else:
    # else, it's not even, so it must be odd
    print("This number is odd")

# if()
