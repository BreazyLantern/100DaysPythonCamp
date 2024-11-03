from inspect import formatargvalues
from operator import contains

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


"""My solution"""
def coffee_machine():
    machine_resources = resources

    def has_resources(m_resources, coffee_entry):
        """Check for resources"""
        menu_item = MENU[coffee_entry]["ingredients"]
        for resource in menu_item:
            if resource in m_resources:
                if m_resources[resource] - menu_item[resource] < 0:
                    print(f"Sorry not enough {resource}")
                    return False
        return True

    def extract_resources(m_resources, coffee_entry):
        """return a modified resource list for resources that were used"""
        menu_item = MENU[coffee_entry]["ingredients"]
        for resource in menu_item:
            if resource in m_resources:
                m_resources[resource] = m_resources[resource] - menu_item[resource]
        return m_resources

    def give_change(payment_amount, coffee_entry):
        """Returns the amount of change from a transaction"""
        return payment_amount - MENU[coffee_entry]["cost"]


    end_program = False

    while not end_program:
        coffee = input("What would you like? (expresso/latte/cappuccino) any other entry "
                       "will stop this program: ").lower()

        if coffee in MENU:
            if has_resources(machine_resources, coffee):
                quarters = int(input("How many quarters?: ")) * .25
                dimes = int(input("How many dimes?: ")) * .10
                nickles = int(input("How many nickles?: ")) * .05
                pennies = int(input("How many pennies?: ")) * .01

                total_amount = quarters + dimes + nickles + pennies
                change = give_change(total_amount, coffee)

                """Should the change be less than 0 it is not a valid transaction"""
                if change >= 0:
                    print(f"Here is your change ${change}.")
                    machine_resources = extract_resources(machine_resources, coffee)
                    print(f"Here is you {coffee}. Enjoy.")
                else:
                    print("Sorry, that is not enough. Money refunded.")
        else:
            end_program = True

coffee_machine()

"""Solution given for this project"""
def program_solution():
    def is_resource_sufficient(order_ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in order_ingredients:
            if order_ingredients[item] > resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins():
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        return total

    def is_transaction_successful(money_received, drink_cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
            global profit
            profit += drink_cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_coffee(drink_name, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ☕️. Enjoy!")

    is_on = True

    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
