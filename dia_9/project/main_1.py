from replit import clear
from art import logo

auctions ={}

def new_bid():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    auctions[name]=bid    
    if answer == 'yes':
        clear()
        new_bid()

print(logo)
print("Wellcome to the secret auction program")
new_bid()
#print(auctions)
max_bid = max(auctions.values())

for values in auctions:
    if auctions[values] == max_bid:
        print("The winner is ",values)
        break
