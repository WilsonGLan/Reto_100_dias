#Calculator
from art import logo 
#Add
def add(n1,n2):
    """Return the sum of two numbers"""
    return n1+n2

#Subtract
def subtract(n1,n2):
    """Return the subtraction of two numbers"""
    return n1-n2

#Multiply
def multiply(n1,n2):
    """Return the multiplication of two numbers"""
    return n1*n2

#Divide
def divide(n1,n2):
    """Return the division of two numbers"""
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    more_operations = True

    while more_operations:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice_operation = input(f"Type 'y' to continue calculation with {answer} or 'n' for exit: ")

        if choice_operation == 'y':
            num1 = answer
        else:
            more_operations = False
            calculator()

calculator()

