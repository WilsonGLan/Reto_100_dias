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

Water = 100
Milk = 50
Coffee = 76
Money = 2.5

turn = True

while turn == True:
    orden = input("what would you like? (espresso/latte/cappuccino):")

    if orden == 'espresso':
        print("espresso")
    elif orden == 'latte':
        print("latte")
    elif orden == 'cappuccino':
        print("cappuccino")


    print("Report")

    print(f"Water: {Water}ml ")
    print(f"Milk: {Milk}ml ")
    print(f"Coffee: {Coffee}ml ")
    print(f"Money: {Money}ml ")

    opcion = input("Would you like to continue? Type 'on' for yes or 'off' for not\t")

    if opcion == 'off':
        turn = False