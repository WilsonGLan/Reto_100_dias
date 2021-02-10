#!/usr/bin/python

import data_coffee as data

water = 0
milk = 0
coffee = 0
cost = 0
turn = True

#def espresso_total(order_client):
    


while turn == True:

    order = input("what would you like? (espresso/latte/cappuccino):")
    if order != 'report':
        #print(data.MENU[orden]["ingredients"])
        list_ingredients = data.MENU[order]["ingredients"].items()
        for ingredients, volume in list_ingredients:
            print(ingredients, "=", volume)
            #if volume < revisar
        

    else:
        water = data.resources["water"] - water
        milk = data.resources["milk"] - milk
        coffee = data.resources["coffee"] - coffee
        
        print(f"water = {water}")
        print(f"milk = {milk}")
        print(f"coffee = {coffee}")

    opcion = input("Would you like to continue? Type 'on' for yes or 'off' for not\t")

    if opcion == 'off':
        turn = False