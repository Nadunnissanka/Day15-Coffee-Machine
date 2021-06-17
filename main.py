# --Coffee machine project--
# Three hot flavours - espresso, latte, cappuccino
# coins operate - penny = 1cent - Dime = 10 cents - Nickel = 5 cents - Quarter = 25 cents
# Has starting resources - water 300ml - milk 200ml - coffee 100g
# counting cup selling
# -- programing requirements --
# 1.print a report.
# 2.check resources sufficient?
# 3.process coins.
# 4.check transaction successful?
# 5.make coffee - resources should reduce.

from machine import MENU
from machine import resources

# loop key
loop_dead = False

# coins
quarter = 0.25
dime = 0.10
nickles = 0.05
pennies = 0.01


def deduct_resources(coffee):
    """This function deduct base resources"""
    if coffee == "espresso":
        water = MENU[coffee]["ingredients"]["water"]
        coffee = MENU[coffee]["ingredients"]["coffee"]

        resources["water"] = resources["water"] - water
        resources["coffee"] = resources["coffee"] - coffee
    else:
        water = MENU[coffee]["ingredients"]["water"]
        milk = MENU[coffee]["ingredients"]["milk"]
        coffee = MENU[coffee]["ingredients"]["coffee"]

        resources["water"] = resources["water"] - water
        resources["milk"] = resources["milk"] - milk
        resources["coffee"] = resources["coffee"] - coffee


def calculate_payment():
    """" This Function Calculate Payment Done By Coins """
    input_quarter = int(input("how many quarters?: "))
    input_dime = int(input("how many dimes?: "))
    input_nickle = int(input("how many nickles?: "))
    input_pennie = int(input("how many pennies?: "))
    payment = (quarter * input_quarter) + (dime * input_dime) + (nickles * input_nickle) + (pennies * input_pennie)
    return payment


def calculate_cost(payment, name):
    """This Function Calculate cost and change"""
    cost = MENU[name]["cost"]
    if payment == cost:
        resources["profit"] = cost
        return 0
    elif payment > cost:
        resources["profit"] = cost
        change = payment - cost
        return change
    else:
        print("Insufficient money. Here is a full refund!")


print("-- Coffee Machine Option (Keywords) --")
print("*. Type 'report' to get a report on resources.")

while not loop_dead:
    # TODO: 1.Espresso maker code
    coffee_option = input("What would you like? (espresso/latte/cappuccino/report or off):")
    if coffee_option == "report":
        print(
            f"Water : {resources['water']}\nMilk : {resources['milk']}\nCoffee : {resources['coffee']}\nProfit : {resources['profit']}")
    elif coffee_option == "off":
        quit()
    elif coffee_option == "espresso":
        espresso_water = MENU["espresso"]["ingredients"]["water"]
        espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
        if resources['water'] >= espresso_water and resources['coffee'] >= espresso_coffee:
            full_payment = calculate_payment()
            customer_change = "{:.2f}".format(calculate_cost(payment=full_payment, name=coffee_option))
            print(f"Here is your change: ${customer_change}")
            deduct_resources(coffee_option)
            print(f"Enjoy your {coffee_option}")
        else:
            print("Insufficient resources!")
    elif coffee_option == "latte":
        # TODO: 2.Latte maker code
        latte_water = MENU["latte"]["ingredients"]["water"]
        latte_milk = MENU["latte"]["ingredients"]["milk"]
        latte_coffee = MENU["latte"]["ingredients"]["coffee"]
        if resources['water'] >= latte_water and resources['coffee'] >= latte_coffee and resources['milk'] >= latte_milk:
            full_payment = calculate_payment()
            customer_change = "{:.2f}".format(calculate_cost(payment=full_payment, name=coffee_option))
            print(f"Here is your change: ${customer_change}")
            deduct_resources(coffee_option)
            print(f"Enjoy your {coffee_option}")
        else:
            print("Insufficient resources!")
    elif coffee_option == "cappuccino":
        # TODO: 3.Cappuccino maker code
        cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
        cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
        cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        if resources['water'] >= cappuccino_water and resources['coffee'] >= cappuccino_coffee and resources['milk'] >= cappuccino_milk:
            full_payment = calculate_payment()
            customer_change = "{:.2f}".format(calculate_cost(payment=full_payment, name=coffee_option))
            print(f"Here is your change: ${customer_change}")
            deduct_resources(coffee_option)
            print(f"Enjoy your {coffee_option}")
        else:
            print("Insufficient resources!")
    else:
        print("Invalid Input!\n")
