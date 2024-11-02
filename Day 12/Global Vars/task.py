# Modifying Global Scope

enemies = 1

""" try avoiding doing this as modifying a scope this way is very unstable for the longevity
of a programs long-term functionality"""

def increase_enemies():
    global enemies # this is the way to modify a
                    # global variable outside the scope of this function

    enemies += 1 # now this variable that is above this function is modifiable
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

"""To properly modify a global function try making a function like below instead or 
a specific function whose purpose is to only modify the value without trying to set the 
global variable"""

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


#Day prev task 4 This was depricated
# Global Constants
PI = 3.14159
GOOGLE_URL = "https://www.google.com/"

def global_const():
    print(GOOGLE_URL)