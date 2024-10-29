print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age? "))
    pay = 0
    if age <= 12:
        pay = 5
    elif age <= 18:
        pay = 7
    else:
        pay = 12

    print(f"Please pay ${pay}")
else:
    print("Sorry you have to grow taller before you can ride.")
