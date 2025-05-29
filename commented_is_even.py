# get user input, convert it to an integer,
# and assign to a variable called "num"
num = int(input("Please enter a positive number: "))

# check to see if num is evenly divisible by 2
if(num % 2 == 0):
    # if yes, print it's even
    print("This number is even")
else:
    # if no, print it's odd
    print("This number is odd")