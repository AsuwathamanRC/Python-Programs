from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

orderCoffee = True

while orderCoffee:
    items = menu.get_items()
    choice = input(f"What would you like? ({items}): ")

    if choice=="off":
        orderCoffee = False
    elif choice=="report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        order = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(order) and moneyMachine.make_payment(order.cost):
            coffeeMaker.make_coffee(order)
