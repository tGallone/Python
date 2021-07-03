from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mm = MoneyMachine()
cm = CoffeeMaker()
menu = Menu()
is_on = True # turn machine on

while is_on: #Whilst the machine is "on"
    options = menu.get_items() # load menu into options variable
    choice = input(f"What would you like? ({options}): ") # store user input into choice
    if choice == "off": # if off is entered, turn off the machine
        is_on = False
    elif choice == "report": # if report is entered
        cm.report() # show coffee machine report
        mm.report() # show money machine report
    else: # if anything else is entered
        drink = menu.find_drink(choice) # pass the choice entered into the find_drink class
        if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost): # if the coffee machine has sufficent supplies and enough money is entered
            cm.make_coffee(drink) # make the drink
    
        