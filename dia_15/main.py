#!/usr/bin/python

import data_coffee as data

cost = 0
turn = True
apply = True

while turn:
    temporary_quantity ={}
    order = input("what would you like? (espresso/latte/cappuccino):")
    if order in ['espresso', 'latte', 'cappuccino']:        
        list_ingredients = data.MENU[order]["ingredients"].items()
        cost = data.MENU[order]["cost"]
        for ingredients, volume in list_ingredients:
            print(ingredients, "=", data.resources[ingredients])            
            if volume > data.resources[ingredients]:
                print(f"There is not enough {ingredients}")
                apply = False
            else:
                temporary_quantity[ingredients] = volume
        if apply:
            elements_temporary = temporary_quantity.items()
            for ingredient_temporal, total in elements_temporary:
                final_total = data.resources[ingredient_temporal] - total
                data.resources[ingredient_temporal] = final_total
                #print(ingredient_temporal, "=", data.resources[ingredient_temporal])
        
                
    elif order == 'report':
        list_report = data.resources.items()
        for ingredients, volume in list_report:
            print(ingredients, "=", data.resources[ingredients])
        print(f"Cost = {cost}")
    else:
        print("ha ingresado una opción incorrecta")

    opcion = input("Would you like to continue? Type 'on' for yes or 'off' for not\t")

    if opcion == 'off':
        turn = False
