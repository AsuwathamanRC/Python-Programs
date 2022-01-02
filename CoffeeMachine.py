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

QUARTERS = 0.25
DIMES = 0.1
NICKLES = 0.05
PENNIES = 0.01

money = 0


def askForCoffee():
    userInput = input("What would you like? (espresso/latte/cappuccino):")  
    return userInput


def checkResource(coffeename):
    requiredWater = MENU[coffeename]['ingredients'].get('water',0)
    requiredMilk = MENU[coffeename]['ingredients'].get('milk',0)
    requiredCoffee = MENU[coffeename]['ingredients'].get('coffee',0)

    if requiredWater<=resources['water'] and requiredMilk<=resources['milk'] and requiredCoffee<=resources['coffee']:
        resources['coffee'] -= requiredCoffee
        resources['water'] -= requiredWater
        resources['milk'] -= requiredMilk
        return True
    elif not requiredWater<=resources['water']:
        print("Sorry there is not enough water.")
        return False
    elif not requiredMilk<=resources['milk']:
        print("Sorry there is not enough milk.")
        return False
    elif not requiredCoffee<=resources['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return False


def processCoins(coffeename):
    global money
    coffeePrice = MENU[coffeename]['cost']

    print(f"Please insert coins (${coffeePrice})")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    userAmount = (quarters*QUARTERS) + (dimes*DIMES) + (nickles*NICKLES) + (pennies*PENNIES)
    money += coffeePrice

    if userAmount<coffeePrice:
        return False

    if userAmount>coffeePrice:
        print(f"Here is ${round(userAmount-coffeePrice,2)} in change.")
    print(f"Here is your {coffeename} ☕. Enjoy!")
    return True


orderCoffee = True
while orderCoffee:
    choice = askForCoffee()

    if choice=="off":
        orderCoffee = False
    elif choice=="refill":
        resources['coffee'] = 100
        resources['milk'] = 200
        resources['water'] = 300
    elif choice=="report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")
    else:
        if checkResource(choice):
            if not processCoins(choice):
                print("Sorry that's not enough money. Money refunded.")