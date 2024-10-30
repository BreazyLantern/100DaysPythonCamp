import random

# Using the imported library from random to generate random numbers
# python module training

# to make new modules right-click on the
# project or subfolder in the project to create a new module
# then select new then select python file
# in this case we select "Random Module", right-click, then select new then python file

# Random integers
print(random.randint(0, 80))

# generate a float between 0 to 1 then multiply by a number to
# increase the bounds outside of one
# semi-open range may or may never get the upper bound
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# same functionality as the above
# may or may not get the upper bound
random_float = random.uniform(1, 10)
print(random_float)

# flipping coin example
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

