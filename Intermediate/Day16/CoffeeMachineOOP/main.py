from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    # TODO: 1. Prompt user what coffee they would like
    choice = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()
    # choice = "latte"
    # TODO: 2. Catch maintenance tasks for 'off', 'report', and invalid options
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice not in coffee_menu.get_items():
        print("Invalid option.")
    # TODO: 4. Check resources of 'choice' and process 'coins' before making the drink
    else:
        drink = coffee_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
