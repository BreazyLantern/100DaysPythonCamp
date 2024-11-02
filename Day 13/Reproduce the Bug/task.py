from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

"""The error in this program is that 6 in not a valid index for the list to retrieve from
if there are 6 entries in the list then the index is 0 to 5, there for if the random int
we get for this function is 6 then we have told the program to retrieve from an invalid
index in the list since that does not exist. Just change the values in the randint to 0 and 5
for this issue"""