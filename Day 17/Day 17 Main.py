
class User:
    # make an empty class
    # pass
    # Using an init will make it so it is required for initialization entries
    # if you want it to not need to input something provide a default value
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # this is defaulting an attribute
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1

# like this
user_1 = User("001", "Terry")
# create attributes
# user_1.id = "001"
# user_1.username = "Terry"

print(user_1.username)

# improper input method
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Terri"

user_2 = User("002", "Jack")
user_2.followers = 5
print(user_1.followers)
print(user_2.followers)



user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
