# regular function example without inputs
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")

greet()

# inputs example
def greet_with_name(name):
    print(f"How do you do {name}")
    print(f"Isn't it nice today, {name}")

greet_with_name("Terry")

greet_with_name(input("Hi what is you name?\n"))