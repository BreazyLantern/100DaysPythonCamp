import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# make a game of rock paper scissors
computer_choice = random.randint(0,2)
game_images = [rock, paper, scissors]

player_choice = int(input("What hand will you play? [rock = 0, paper = 1, scissors = 2]\n"))
if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)

print(f"The computer played:\n{game_images[computer_choice]}")

if player_choice >= 3 or player_choice < 0:
    print("Invalid input you lose")
elif player_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and player_choice == 2:
    print("You lose")
elif computer_choice > player_choice:
    print("You lose")
elif player_choice > computer_choice:
    print("You win")
elif computer_choice == player_choice:
    print("It's a tie")
