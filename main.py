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


def resource():
   return f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}"

# TODO 3: create a function to add all four coin




def add_coin():
    """adding all coin"""
    penny = int(input("number of penny : "))
    dime = int(input("number of dime : "))
    nickel = int(input("number of nickel : "))
    quarter = int(input("number of quarter : "))

    total_penny = penny*0.01
    total_dime = dime*0.10
    total_nickel = nickel*0.05
    total_quarter = quarter*0.25

    total_cost = total_dime + total_penny + total_nickel + total_quarter

    return total_cost



# TODO 4: checking if money is sufficient or not


def change():
    """checking if money is sufficient or not and returning changes"""
    if coffee_button == "espresso":
        if add_coin() >= 1.5 :
            changes = add_coin() - 1.5
        else:
            print("do not have enough money")
    elif coffee_button == "latte":
        if add_coin() >= 2.5 :
            changes = add_coin() - 2.5
        else:
            print("do not have enough money")
    elif coffee_button == "cappuccino":
        if add_coin() >= 3.5 :
            changes =add_coin() - 3.5
        else:
            print("do not have enough money")
    return changes



# TODO 1 :let's take input from user what they want to do
coffee_button = input("What would you like? (espresso/latte/cappuccino):").lower()

# TODO 2 :check whether they want report or coffee
if coffee_button == "report":
    print(resource())

if coffee_button == "espresso":
    if change():
        print("enjoy your coffee")
        print(change())



