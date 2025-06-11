import random
import AsciiSymbols

#NOTE this is outdated from the original course, but I made my own python file to do this example anyway.
#Found the Ascii art from a search on the web and included it into another python file to import here.

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
print(AsciiSymbols.hand_symbols[user_choice][0])

computer_choice = random.choice(AsciiSymbols.hand_symbols)

print(f"Computer chose {computer_choice[0]}")


lose = "User lost!"
win = "User wins!"
#invalid input
if user_choice > 2 or user_choice <0:
    print("Invalid input. You lose.")
#rock vs scissors
elif user_choice == 0 and computer_choice[1] == 2:
    print(win)
elif computer_choice[1] == 0 and user_choice == 2:
    print(lose)
elif computer_choice[1] > user_choice:
    print(lose)
elif user_choice > computer_choice[1]:
    print(win)
elif computer_choice[1] == user_choice:
    print("It's a draw!")