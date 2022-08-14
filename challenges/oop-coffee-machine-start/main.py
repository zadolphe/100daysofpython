from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

resources = {
    "Water": 300,
    "Milk": 100,
    "Coffee": 100,
}

#functions
def calculateValue(coin):
    total = 0.00
    if coin == "dime":
        total += .10
    elif coin == "nickel":
        total += .05
    elif coin == "quarter":
        total += .25

    return total

#instantiate objects
moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    userInput = input("What would you like? (espresso, latte or cappuccino? ")
    if userInput == "off":
        is_on = False
    elif userInput == "report":
        moneyMachine.report()
        coffeeMaker.report()
        #print("Water ", resources['Water'], "ml\n", resources['Milk'], "ml\n", resources['Coffee'], "ml\n", cashProfit,"\n")  
    else:
        #do a bunch of stuff 
        drinkChoice = menu.find_drink(userInput)
        inputCheck = coffeeMaker.is_resource_sufficient(drinkChoice)
        if(inputCheck):
            if(moneyMachine.make_payment(drinkChoice.cost)):
                coffeeMaker.make_coffee(drinkChoice)
                is_on = False
        else:
            print("Pease enter what you would like: ")
