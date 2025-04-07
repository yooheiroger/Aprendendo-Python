from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True
while machine_is_on:
    print()
    option = (menu.get_items())
    choice = input(f'what do you like? {option}:  \n')
    if choice == 'off':
        machine_is_on = False
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        coffee = (menu.find_drink(choice))
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)






