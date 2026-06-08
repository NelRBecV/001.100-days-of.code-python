# Coffee Machine Project

def coffee_menu():
    recipes = [{
        'name': 'espresso',
        'water': 50,
        'milk': 0,
        'coffee': 18,
        'money': 1.5},
        {
        'name': 'cappuccino',
        'water': 200,
        'milk': 150,
        'coffee': 24,
        'money': 2.5},
        {
        'name': 'latte',
        'water': 250,
        'milk': 150,
        'coffee': 24,
        'money': 3.0
    }]
    return recipes


def storage():

    supplies = {
        'water': 300,
        'milk': 200,
        'coffee': 100,
        'money': 0
    }

    return supplies


def drink_available(drink_water, drink_coffee, drink_milk):
    if drink_water >= 0:
        if drink_coffee >= 0:
            if drink_milk >= 0:
                make_drink = True
            else:
                print("There is no enough milk")
                make_drink = False
        else:
            print("There is no enough coffee")
            make_drink = False
    else:
        print("There is no enough water")
        make_drink = False

    return make_drink


# TODO-9: The machine has to show the main menu in order to be ready for another sale.
machine_menu = ['off', 'report', 'espresso', 'cappuccino', 'latte']
machine_working = "on"
deliver = {}
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
            print("Milk: {ingredients['milk']}ml")
            print("Coffee: {ingredients['coffee']}gr")
            print("Money: ${ingredients['money']})                    
        else:
  
          # TODO-4: Create a function to check if the user's beverage can be done
            recipe = coffee_menu()
      
            for i in range(len(recipe)):
                if recipe[i]['name'] == user_choice:
                    deliver = recipe[i]
            
            water_sale = ingredients['water'] - deliver['water']
            coffee_sale = ingredients['coffee'] - deliver['coffee']
            milk_sale = ingredients['milk'] - deliver['milk']
            money_sale = ingredients['money'] + deliver['money']
            
            # TODO-5: A prompt must be displayed to introduce the money. Only coins can be used to cash the product.
            if drink_available(water_sale, coffee_sale, milk_sale,):
                pennies = int(input("How many pennies?: "))
                nickels = int(input("How many nickles?: "))
                dimes = int(input("How many dimes?: "))
                quarters = int(input("How many quarters?: "))
            
              # TODO-6: Confirm the user's payment is enough to carry on with the transaction
                tot_money = float((pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25))
              
                if tot_money < deliver['money']:
                    print("There is not enough money to finish the transaction. Money Refund!!!")
                else:
                    # TODO-7: Make the coffee
                    ingredients = {'water': water_sale, 'milk': milk_sale, 'coffee': coffee_sale, 'money': money_sale}
                    
                    if tot_money > deliver['money']:
                        change = tot_money - deliver['money']
                        print(f"Here is your change: ${change:.2f}")
                      
                    # TODO-8: Prompt a message to confirm the end of transaction
                    print(f"Here is your {deliver['name'].capitalize()} ☕. Enjoy it!!!")
    else:
        print("Command not found")
