import random

import art

# creating the black jack game
# Deck is unlimited in size
# no jokers
# Jack, Queen, King = 10
# Ace is 1 or 11

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.choice(cards)]


def calculate_score(cards):
    """Take a list of cards and returns a score from the sum total of the list of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, computer_score):
    if u_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > computer_score:
        return "You win 😀"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo)
    player_cards = []
    computers_cards = []
    computers_score = -1
    user_score = -1
    is_game_over = False

    player_cards.extend([deal_card(), deal_card()])
    computers_cards.extend([deal_card(), deal_card()])
    while not is_game_over:


        user_score = calculate_score(player_cards)
        computers_score = calculate_score(computers_cards)

        print(f"Your cards: {player_cards}, current score: {user_score}")
        print(f"Computer's first card: {computers_cards[0]}")

        if user_score == 0 or computers_score == 0 or user_score >= 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computers_score != 0 and computers_score < 17:
        computers_cards.append(deal_card())
        computers_score = calculate_score(computers_cards)

    print(f"Your final hand: {player_cards}, final score: {user_score}")
    print(f"Computer's final hand {computers_cards}, final score: {computers_score}")
    print(compare(user_score, computers_score))

while input("Do you want to play a game of Blackjack? 'y'/'n': ") == "y":
    print("\n" * 20)
    play_game()