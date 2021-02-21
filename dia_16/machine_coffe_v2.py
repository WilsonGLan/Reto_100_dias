#!/usr/bin/python

import data_coffee as data

cost = 0
turn = True
money_entered = 0
remaining_money = 0

while turn:
    temporary_quantity ={}
    apply = True        
    order = input("what would you like? (espresso/latte/cappuccino):")
    if order in ['espresso', 'latte', 'cappuccino']:        
        list_ingredients = data.MENU[order]["ingredients"].items()
        cost = data.MENU[order]["cost"]
        #iterar ingredientes para evaluar si hay suficiente para atender el pedido
        for ingredients, volume in list_ingredients:
            mesure = 'g' if ingredients == 'coffee' else 'ml'
            print(f"{ingredients} = {data.resources[ingredients]}{mesure}")            
            if volume > data.resources[ingredients]:
                print(f"There is not enough {ingredients}")
                apply = False
            else:
                temporary_quantity[ingredients] = volume
        if apply:
            coin_distribution = data.coins_value.items()
            print(f"Cost = ${cost}")
            print(f"Money entered = ${money_entered}")
            print(f"Remaining money = ${remaining_money}")
            print("==================================================================")
            #Suma el dinero ingresado para comprar el pedido
            for coin, value_coin in coin_distribution:                
                number_coin = int(input(f"How many {coin} you enter \t"))
                sum_coin = value_coin * number_coin
                money_entered += sum_coin
                money_entered = float("{0:.2f}".format(money_entered))
                print(f"Coin entered = ${sum_coin}")  
            money_entered += remaining_money
            print(f"Money entered = ${money_entered}")  
            if cost <= money_entered:
                #calcula cuanto dinero sobra
                remaining_money = money_entered - cost
                remaining_money = float("{0:.2f}".format(remaining_money))
                money_entered = 0#remaining_money
                elements_temporary = temporary_quantity.items()
                for ingredient_temporal, total in elements_temporary:
                    final_total = data.resources[ingredient_temporal] - total
                    data.resources[ingredient_temporal] = final_total
                    #print(ingredient_temporal, "=", data.resources[ingredient_temporal])
            else:
                print("Sorry that's not enough money. Money refunded.")
                
    if order == 'report':
        list_report = data.resources.items()
        for ingredients, volume in list_report:
            mesure = 'g' if ingredients == 'coffee' else 'ml'
            print(f"{ingredients} = {data.resources[ingredients]}{mesure}")
        print(f"Cost = ${cost}")
        print(f"Remaining money = ${remaining_money} ")

    if order not in ['espresso', 'latte', 'cappuccino', 'report']:
        print("ha ingresado una opción incorrecta")
    print("==================================================================")    
    opcion = input("Would you like to continue? Type 'on' for yes or 'off' for not\t")

    if opcion == 'off':
        turn = False
