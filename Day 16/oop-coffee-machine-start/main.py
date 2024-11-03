from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Please refer to documentation on all object classes to understand what they each have and how to use them
# PycharmProjects\100 Days of Code - The Complete Python Pro Bootcamp\Day 16\oop-coffee-machine-start/Coffee+Machine+Classes+Documentation

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
