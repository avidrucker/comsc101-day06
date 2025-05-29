import time

some_string = "Follow the white rabbit, Neo."

for char in some_string:
    # flush=True means to print without waiting
    # end="" means to not print a newline after char
    print(char, end="", flush=True)
    # pause the program for 0.1 seconds
    time.sleep(0.1)