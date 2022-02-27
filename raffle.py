'''Importing '''
import random
'''Declare list'''
names = []
'''Loop to get valid prize input'''
prize_input_loop = True
while prize_input_loop:
    prize = input("Welcome to the best raffle you've ever seen, literally.\nPlease enter the prize to be won: ")
    if len(prize) == 0:
        print("Please enter a prize to be won: ")
    else:
        prize_input_loop = False
'''Loop to get valid prize cost input'''
prize_cost_loop = True
while prize_cost_loop:
    try:
        prize_cost = input("How valuable is the prize?(in $'s, do not add the $ symbol): ")
        if len(prize_cost) == 0:
            print("Please enter the value of the prize to be won: ")   
        else:
            prize_cost_loop = False
    except:
        print("Please enter a valid integer prize value (in $'s, do not add the $ symbol)")
'''Run loop to append viable input names and remove empty answers'''
print ("Please enter the names of people entering the raffle:")
name_input_loop = True
while input_loop:
    try:
        name = input()
        if name == "end":
            input_loop = False
        elif len(name) == 0:
            print ("Input empty, please enter the names of people entering the raffle:")
        else:
            names.append(name)
    except:
        print ("Please enter a valid name")
'''Get random number between 0 and one less than the length of the list, used to determine random winner'''
winner = random.randint(0, len(names) - 1)
'''Print winner'''
print(f"All names have now been entered...\nThe winner of the {prize} worth ${prize_cost} is...{names[winner]}!")

