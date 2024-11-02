import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


# Use a break point to debug in this program click on the left side number lines then press
# bug execution icon top right to start debug mode
"""The reason for the printed list being wrong is how in the function we are affecting and 
appending the entries. Debugging through the code when we get into the for loops body
we modify the first value of the a_list and save that to a variable then continue modifying 
that variable all through out the running of the for loop then we append that continuously modified
variable as the only entry to b_list. In the end it comes down to an indentation error
for where we append the value"""