# SDM: The fizzbuzz program will
# print out the numbers from 1 to 100
# but, instead of printing multiples
# of 3, we will instead print "fizz"
# and instead of printing multiples
# of 5, we will instead print "buzz"
# so, if a number is divisible by
# both 5 *and* 3, then we will print
# "fizzbuzz"

# approaches
# - make a list of 100 numbers (we can use range() for this)
# - write down the steps we will take "pedestrian approach"
# - write some conditional logic (we can use if/else or if/elif/else blocks for this)
# - print out to the terminal a single number

# one approach would be to manually
# type out all the print statements
# print(1)
# print(2)
# print("fizz")

# change 21 to 101 when you're ready
for num in range(1, 101):
    # if num is evenly divisible by 3
    if(num % 3 == 0 and num % 5 == 0):
        print("fizzbuzz")
    elif(num % 3 == 0):
        print("fizz")
    elif(num % 5 == 0):
        print("buzz")
    else:
        print(num)