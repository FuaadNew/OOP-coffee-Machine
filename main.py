from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

on= True
while on:
    choice = input("“What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink= menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
