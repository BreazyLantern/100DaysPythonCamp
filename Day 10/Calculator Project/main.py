import art


def add(n1, n2):
    return n1 + n2

def mult(n1, n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return  n1 / n2


# call a function with a different name
# favfunc = add
#
# print(favfunc(1,2))

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": mult,
}

# print(operations["*"](4,8))

# recursion
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number?: "))

        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new operation")

        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()