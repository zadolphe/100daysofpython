from tkinter import Menu


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": .05,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": .5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 0.60,
    }
}

#global variables 
cashProfit = 0.00
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


#espresso: 50ml water and 18g coffee
#latte: 200ml water, 24g coffee and 150ml milk
#cappuccino: 250ml water, 24g coffee and 100ml milk 
def resourcesSufficient(the_input):
    is_sufficient = True
    #espresso
    if the_input == "espresso":
        #check if enough water 
        if resources["Water"] < MENU[the_input]['ingredients']['water']:
            print("there is not enough water")
            is_sufficient = False
            #check if enough coffee 
        if resources["Coffee"] < MENU[the_input]['ingredients']['coffee']:
            print("there is not enough coffee")
            is_sufficient = False
    #latte
    elif the_input == "latte":
        #check if enough water 
        if resources["Water"] < MENU[the_input]['ingredients']['water']:
            print("there is not enough water")
            is_sufficient = False
            #check if enough coffee 
        if resources["Coffee"] < MENU[the_input]['ingredients']['coffee']:
            print("there is not enough coffee")
            is_sufficient = False
            #check if enough milk
        if resources['Milk'] < MENU[the_input]['ingredients']['milk']:
            print("not enough milk!")
            is_sufficient = False
    #cappuccino
    elif the_input == "cappuccino":
        #check if enough water 
        if resources["Water"] < MENU[the_input]['ingredients']['water']:
            print("there is not enough water")
            is_sufficient = False
            #check if enough coffee 
        if resources["Coffee"] < MENU[the_input]['ingredients']['coffee']:
            print("there is not enough coffee")
            is_sufficient = False
            #check if enough milk
        if resources['Milk'] < MENU[the_input]['ingredients']['milk']:
            print("not enough milk!")
            is_sufficient = False
    else: 
        is_sufficient = False
    return is_sufficient
        
                

is_on = True
while is_on:
    userInput = input("What would you like? (espresso, latte or cappuccino? ")
    if userInput == "off":
        is_on = False
    elif userInput == "report":
        print("Water ", resources['Water'], "ml\n", resources['Milk'], "ml\n", resources['Coffee'], "ml\n", cashProfit,"\n")  
    else:
        #check if the input is proper and if resources are sufficient, see function 
        inputCheck = resourcesSufficient(userInput)
        if(inputCheck):
            #prompt user to insert coins which takes a string of dime, quarter, nickle
            coinInput1 = input("please insert coins: ")
            coinInput2 = input("please insert second coin: ")
            coinInput3 = input("please insert third coin: ")

            #call calculate value function to calculate total monetary value 
            value = 0
            value += calculateValue(coinInput1)
            value += calculateValue(coinInput2)
            value += calculateValue(coinInput3)

            #if value is not enough money for drink, prompt to say not enough sorry and return the coins 
            if value < MENU[userInput]['cost']:
                print("sorry not enough moeny, coins refunded")
            elif value == MENU[userInput]['cost']:
                cashProfit += MENU[userInput]['cost']
                remaining = value - MENU[userInput]['cost']
                print("please take ", remaining, "in change")
                
                #now if transaction successful, deduct the resources from the ingredients 
                resources['Water'] = resources['Water'] - MENU[userInput]['ingredients']['water']
                resources['Coffee'] = resources['Coffee'] - MENU[userInput]['ingredients']['coffee']
                if(userInput!="espresso"):
                    resources['Milk'] = resources['Milk'] - MENU[userInput]['ingredients']['milk']
                print("Water ", resources['Water'], "ml\n", resources['Milk'], "ml\n", resources['Coffee'], "ml\n", cashProfit,"\n")
                print("Here is your ", userInput, " enjoy!")
                is_on = False
            else:
                cashProfit += MENU[userInput]['cost']
                remaining = value - MENU[userInput]['cost']
                print("please take ", remaining, "in change")
                
                #now if transaction successful, deduct the resources from the ingredients 
                resources['Water'] = resources['Water'] - MENU['espresso']['ingredients']['water']
                resources['Coffee'] = resources['Coffee'] - MENU['espresso']['ingredients']['coffee']
                if(userInput!="espresso"):
                    resources['Milk'] = resources['Milk'] - MENU[userInput]['ingredients']['milk']
                print("Water ", resources['Water'], "ml\n", resources['Milk'], "ml\n", resources['Coffee'], "ml\n", cashProfit,"\n")
                
                print("Here is your ", userInput, " enjoy!")
                is_on = False
        else:
            print("Please enter a drink (espresso, latte or cappuccino) ")


