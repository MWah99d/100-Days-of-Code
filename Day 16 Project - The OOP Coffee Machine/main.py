from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_list = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    drink = input(f"What would you like? ({menu_list.get_items()}): ").lower()
    if drink == "off":
        break
    elif drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu_list.find_drink(drink)
        if menu_item is None:
            break
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)
