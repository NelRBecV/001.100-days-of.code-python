from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_menu = Menu()
coffee_machine_maker = CoffeeMaker()
coins_processor = MoneyMachine()
machine_on = True

while machine_on:
    menu_choices = coffee_machine_menu.get_items()
    user_input = input(f"What would you like ({menu_choices}): ").lower()
    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        coffee_machine_maker.report()
        coins_processor.report()
    elif user_input in menu_choices:
        client_choice = coffee_machine_menu.find_drink(user_input)
        if coffee_machine_maker.is_resource_sufficient(client_choice):
            if coins_processor.make_payment(client_choice.cost):
                coffee_machine_maker.make_coffee(client_choice)
    else:
        print("Command or choice not found.")
