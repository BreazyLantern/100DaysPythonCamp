enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
"""This will result in 2 and 1 in terms of output because of scope"""

# Local scope example
# def drink_potion():
#     potion_strength = 2 # this value will only exist within this function
#     print(potion_strength)
#
# drink_potion()

# global scope example
player_health = 10 # Global variable

def drink_potion():
    potion_strength = 2 # Local variable
    print(potion_strength)

drink_potion()
print(player_health)
