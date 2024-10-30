# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")


def greet_with(name = "Terry", location = "Ohio"):
    print(f"Hello {name}")
    print((f"What is it like in {location}"))

greet_with("Nick", "Los Angeles")

# switching around values example
greet_with(location= "Sucrose", name= "Balaka")


# my method from challenge
# def calculate_love_score(name1, name2):
#     combined = name1 + name2
#     compare_true = ["T", "R", "U", "E"]
#     int_true = []
#
#     for i in range(len(compare_true)):
#         count = 0
#         for j in range(len(combined)):
#             if combined[j].lower() == compare_true[i].lower():
#                 count += 1
#         int_true.append(count)
#
#     compare_love = ["L", "O", "V", "E"]
#     int_love = []
#     for i in range(len(compare_love)):
#         count = 0
#         for j in range(len(combined)):
#             if combined[j].lower() == compare_love[i].lower():
#                 count += 1
#         int_love.append(count)
#
#     print(f"{sum(int_true)}{sum(int_love)}")
#     # TODO: write code...
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")


# method from challenge solution
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")
# Did not now a count was already built in python good to remember.

