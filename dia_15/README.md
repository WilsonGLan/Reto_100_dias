Program Requirements:

1. Print Report
2. Check resources sufficient?
3. Process coins.
4. Check transaction successful?
5. Make coffe


1. Prompt user by asking "what would you like? (espresso/latte/cappuccino)L:"

  a. Check the user's input to decide what to do next.

  b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

2. Turn of the Coffee Machine by entering "off" to the prompt

  a. For maintainers of the coffee machine, they can use "off" as the secret word to turn off the machine. Your code should end execution when this happens.

3. Print report.

  a. When the user enters "report" to the prompt, a report should be generated that shows the current resource values. e.g.

  * Water: 100ml
  * Milk: 50ml
  * Coffee: 76g
  * Money: $2.5

4. Check resources sufficient?

  4.1. When the user chooses a drink, the program should check if there are enough resources to make that drink.

  4.2. E.g. if Latte requires 200 ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: "Sorry there is not enough water."

  4.3. The same should happen if another resource is depleted, e.g. milk or coffee.
  
5. Process coins.

  5.1. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.

  5.2. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

  5.3. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25+0.1x2+0.05+0.01x2 = $0.52

6. Check transaction successful?

  6.1. Check that the user has inserted enough money to purchase the drink they selected. E.g. Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say "Sorry that's not enough money. Money refunded.".

  6.2. But if the user inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time "report" is triggered. E.g.

  * Watter: 100ml
  * Milk:50ml
  * Coffee: 76g
  * Money: $2.5

7. Make Coffee

  7.1. If the transaction is successful and there are enogh resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
  
  7.2. E.g. report before purchasing latte:

  * Watter: 300ml
  * Milk:200ml
  * Coffee: 100g
  * Money: $0

  7.3. Report after purchasing latte:

  * Watter: 100ml
  * Milk:50ml
  * Coffee: 76g
  * Money: $2.5