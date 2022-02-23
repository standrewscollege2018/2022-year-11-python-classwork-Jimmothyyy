import random
'''Declare list'''
names = []
'''Declare variables'''
'''Run loop to append viable input names and remove empty answers'''
print ("Please enter the names of people entering the raffle:\n")
input_loop = True
while input_loop:
    try:
        name = input()
        if name == "stop":
            input_loop = False
        elif len(name) == 0:
            print ("Input empty, please enter the names of people entering the raffle:\n")
        else:
            names.append(name)
print (names)


