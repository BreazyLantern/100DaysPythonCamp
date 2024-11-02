from random import randint

import art

print(art.logo)
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#
# r_num = randint(1,100)
# # print(r_num)
# chances = 0
#
# if difficulty == "easy":
#     chances = 10
# elif difficulty == "hard":
#     chances = 5
#
# def compare_guess(guess_number):
#     print(r_num)
#     if guess_number < r_num:
#         print("Too Low")
#         return False
#     elif guess_number > r_num:
#         print("Too High")
#         return False
#     elif guess_number == r_num:
#         print(f"You got it the answer was {r_num}")
#         return  True
#
# while True:
#     print(f"You have {chances} attempts remaining to guess the number.")
#     guess = int(input("Make a guess: "))
#     # print(guess)
#
#     if compare_guess(guess):
#         chances = 0
#         return
#
#     if chances == 0:
#         print("You've run out of guesses. Refresh to start again.")
#         return
#     else:
#         chances -= 1
#         print("Guess again.")

"""My solution above """

"""Solution by the course below"""

# Constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# compare function
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess returns number of chances left"""
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! the answer was {actual_answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # random number generated
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempt remaining to the guess the number.")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return


game()
