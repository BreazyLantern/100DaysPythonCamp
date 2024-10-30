import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# print out a random name from the list using randoms choice function
print(random.choice(friends))

# option 2
print(friends[random.randint(0, 4)])

