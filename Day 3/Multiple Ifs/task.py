print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Children pay $5.")
    elif age <= 18:
        bill = 7
        print("Youths pay $7.")
    else:
        bill = 12
        print("Adults pay $12.")

    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        # adds $3 to bill
        bill += 3

    print(f"Your total comes up to ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
