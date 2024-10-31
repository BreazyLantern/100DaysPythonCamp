from random import random, randint
from symbol import return_stmt

import art

# creating the black jack game
# Deck is unlimited in size
deck = {}

# no jokers
# Jack, Queen, King = 10
# Ace is 1 or 11

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def random_card():
    return cards[randint(0, len(cards) - 1)]

start_game = True
while start_game:
    player_cards = []
    computers_cards = []

    print(art.logo)
    play_game = input("Do you want to play black jack? y/n: ").lower()
    if play_game == "n":
        break

    # player_cards.extend([random_card(),random_card()])
    player_cards.extend([11, 10])
    computers_cards.append(random_card())

    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {computers_cards[0]}")

    if(sum(player_cards) == 21):
        print("You win with 21!")