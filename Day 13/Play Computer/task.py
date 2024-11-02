year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

"""The bug in this program is that it will only be able to print out for entries that are between 
1980 and 1994 or greater than 1994. How ever it does not have prints for when the input is 
exactly 1994 nore when it is lower or equal to 1980.
Just place a conditional for if they are equal to those values"""