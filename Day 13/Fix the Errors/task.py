# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")


"""The problem in this program is that the if statements body is not indented
for it to properly print out the message and the message itself
is trying to print out with an f string when it is just a string so it will never display
age properly"""

# try block example for wrong inputs
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical entry")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")

