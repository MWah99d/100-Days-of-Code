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
profit = 0


def check_resources_sufficient():
    for key in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def process_coins():
    coins = int(input("Please insert coins.\nHow many quarters?: ")) * 0.25
    coins += int(input("How many dimes?: ")) * 0.1
    coins += int(input("How many nickles?: ")) * 0.05
    coins += int(input("How many pennies?: ")) * 0.01
    return coins


def check_transaction_successful():
    global profit
    if purchase < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        profit += MENU[drink]["cost"]
        if purchase > MENU[drink]["cost"]:
            change = round(purchase - MENU[drink]["cost"], 2)
            print(f"Here is ${change} dollars in change.")
        return True


def make_coffee():
    for key in MENU[drink]["ingredients"]:
        resources[key] -= MENU[drink]["ingredients"][key]
    print(f"Here is your {drink} ☕. Enjoy!")


while True:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "off":
        break
    elif drink == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        enough_resources = check_resources_sufficient()
        if enough_resources:
            purchase = process_coins()
            successful_transaction = check_transaction_successful()
            if successful_transaction:
                make_coffee()
    else:
        print("Invalid choice, please enter valid info.")
