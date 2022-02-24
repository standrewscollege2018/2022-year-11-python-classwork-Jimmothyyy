'''Importing '''
import random
'''Declare list'''
names = []
prize = input("Welcome to the best raffle you've ever seen, literally.\nPlease enter the prize to be won: ")
prize_cost = input("How valuable is the prize?(in $'s, do not add the $ symbol): ")
'''Run loop to append viable input names and remove empty answers'''
print ("Please enter the names of people entering the raffle:")
input_loop = True
while input_loop:
    try:
        name = input()
        if name == "stop":
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
print(f"All names have now been entered...\nThe winner of the{prize} worth ${prize_cost} is...{names[winner]}!")


