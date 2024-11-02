import random

import art
import game_data

"""My solution to this project"""
# game function container
def game():

    # retrieve data list
    data_set = game_data.data

    # initialize boolean for while loop
    game_over = False

    """This function is responsible for formating the list data retrieved into a string 
    output for display"""
    def format_entry(data_set_entry):
        name = data_set_entry["name"]
        description = data_set_entry["description"]
        country = data_set_entry["country"]
        return f"{name} Camello, a {description}, from {country}"

    # initial entry and score value
    entry_a = random.choice(data_set)
    score = -1

    """This function is used to compare the follower count of two inputs from the data set
    then return the string value to compare with the user's entry"""
    def compare_entries(data1, data2):
        data1_followers = data1["follower_count"]
        data2_followers = data2["follower_count"]
        if data1_followers > data2_followers:
            return "a"
        else:
            return "b"


    while not game_over:
        print(art.logo)
        # display message after first proper entry by player
        # note that since we are starting from -1 we should increment the value
        if score >= 0:
            print(f"That's right. Current score {score}")
        else:
            score += 1

        # display entry A followed by entry b
        print(f"Compare A: {format_entry(entry_a)}")
        print(art.vs)
        entry_b = random.choice(data_set)

        # safe check for if these entries are the same
        while entry_b == entry_a:
            entry_b = random.choice(data_set)

        # display entry B
        print(f"Compare B: {format_entry(entry_b)}")

        # acquire player's input
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Compare input to answer
        if user_guess == compare_entries(entry_a, entry_b):
            score += 1
            entry_a = entry_b
        else:
            game_over = True
        # move to new space
        print("\n" * 20)

    # display after game ends
    print(art.logo)
    print(f"Sorry, That's wrong. Final score: {score}")


# call the game
game()

"""Solution from project"""
def project_solution():
    def format_data(account):
        """Takes the account data and returns the printable format."""
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"

    """Note that the original solution posted in this course had a typo
            with the check answer being used wrong this is my revision to make it work"""
    def check_answer(p_guess, a_followers, b_followers):
        """Take a user's guess and the follower counts and returns if they got it right."""
        if a_followers > b_followers:
            return p_guess == "a"
        else:
            return p_guess == "b"

    print(art.logo)
    score = 0
    game_should_continue = True
    # Generate a random account from the game data
    account_b = random.choice(game_data.data)

    # Make the game repeatable.
    while game_should_continue:

        # Making account at position B become the next account at position A.
        account_a = account_b
        account_b = random.choice(game_data.data)

        if account_a == account_b:
            account_b = random.choice(game_data.data)

        print(f"Compare A: {format_data(account_a)}.")
        print(art.vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Clear the screen
        print("\n" * 20)
        print(art.logo)

        # - Get follower count of each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if user is correct.

        is_correct = check_answer(guess,a_follower_count, b_follower_count)

        # Give user feedback on their guess.
        # score keeping.
        if is_correct:
            score += 1
            print(f"You're right! Current score {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_should_continue = False

# project_solution()