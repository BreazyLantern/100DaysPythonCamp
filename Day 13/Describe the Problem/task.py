def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
"""The loop is going from within the range of 1 to 20 but 20 in the range is more like a 
ceiling for the loop
so i will never become 20, range functions never actually return the maximum you put in"""
# 2. When is the function meant to print "You got it"?
""" it is meant to be print out at the end of the loop with i has become 20 but they wont reach
since the range is never going to return 20 range only returns numbers starting from 1
and before 20"""
# 3. What are your assumptions about the value of i?
"""i will be become any number between 1 and 20 but never be 20"""
