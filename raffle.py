'''Importing '''
import random
'''Declare list'''
names = []
print("Welcome to the best raffle you've ever seen, literally.\nPlease enter the name of each contestant once for each time they wish to put their name in")
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



