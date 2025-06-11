total = 0
for number in range(1, 100):
    total += number
print(total)

#Gaussian mathematics theory when given a range of numbers such as 1 to 10 and finding the sum of said number
#the quick way of doing so is to take the beginning and end of the number such as 1 and 10 and getting the sum
# then multiply that sum with half of the largest number. 11 * 5 == 55
# 1 to 100 is 101 * 50 = 5050

# should you find the number is a bit odd like say 1 to 9 then you can still do this but subtract 1 from the half of
# the largest number rounded up then add that back into the equation. 1 to 9 is 10 * (5 -1) + 5 = 45
# 1 to 29 is 30 * (15 - 1) +15 = 435