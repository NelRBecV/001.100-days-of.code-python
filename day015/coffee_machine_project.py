# Coffee Machine Project

def coffee_menu(deliver: str):
    recipes = {
        'espresso': {
            'water': 50,
            'milk': 0,
            'coffee': 18,
            'cost': 1.5
        },
        'cappuccino': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
            'cost': 2.5
        },
        'latte': {
            'water': 250,
            'milk': 150,
            'coffee': 24,
            'cost': 3.0
        }
    }
    return recipes[deliver]


def storage():  # For initialization values purpose only
    supplies = {
        'water': 300,
        'milk': 200,
        'coffee': 100,
        'money': 0
    }
    return supplies


def process_coins() -> float:
    pennies = int(input("How many pennies?: "))
    nickels = int(input("How many nickles?: "))
    dimes = int(input("How many dimes?: "))
    quarters = int(input("How many quarters?: "))

    # TODO-6: Confirm the user's payment is enough to carry on with the transaction
    return (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25)


def drink_available(drink_chosen: dict, inventory: dict) -> bool:
    if inventory['water'] - drink_chosen['water'] >= 0:
        if inventory['milk'] - drink_chosen['milk'] >= 0:
            if inventory['coffee'] - drink_chosen['coffee'] >= 0:
                return True
            print("There is no enough coffee")
            return False
        print("There is no enough milk")
        return False
    print("There is no enough water")
    return False


# TODO-9: The machine has to show the main menu in order to be ready for another sale.
machine_menu = ['off', 'report', 'espresso', 'cappuccino', 'latte']
machine_working = "on"
ingredients = storage()
while machine_working == "on":
    # TODO-1: Show a menu where the user can choose what he/she want to drink
    user_choice = input("What would you like?(espresso\\latte\\cappuccino): ").lower()
    if user_choice in machine_menu:
        # TODO-2: Create an option to turn the machine off
        if user_choice == "off":
            machine_working = "off"
        # TODO-3: The machine must be able to print the ingredients' inventory as well as the selling earnings
        elif user_choice == "report":
            print(f"Water: {ingredients['water']}ml")
            print(f"Milk: {ingredients['milk']}ml")
            print(f"Coffee: {ingredients['coffee']}gr")
            print(f"Money: ${ingredients['money']}")
        else:
            # TODO-4: Create a function to check if the user's beverage can be done
            menu_option = coffee_menu(user_choice)
            if drink_available(menu_option, ingredients):
                # TODO-5: A prompt must be displayed to introduce the money. Only coins can be used to cash the product.
                client_payment = process_coins()
                if client_payment < menu_option['cost']:
                    print("There is not enough money to finish the transaction. Money Refund!!!")
                else:
                    # TODO-7: Make the coffee
                    ingredients['water'] -= menu_option['water']
                    ingredients['milk'] -= menu_option['milk']
                    ingredients['coffee'] -= menu_option['coffee']
                    ingredients['money'] += menu_option['cost']
                    change = client_payment - menu_option['cost']
                    print(f"Here is your change: ${change:.2f}")
                    # TODO-8: Prompt a message to confirm the end of transaction
                    print(f"Here is your {user_choice.capitalize()} ☕. Enjoy it!!!")
    else:
        print("Command not found")
