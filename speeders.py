'''Declare lists'''
names = []
fines = []
'''Start code loop'''
print("Welcome officer,\nPlease enter names to check for arrest warrants and calculate fines.")
code_loop = True
while code_loop:
    '''Start name loop'''
    name_loop = True
    while name_loop:
        try:
            name = str(input("Speeders name: "))
            if name == "John Smith" or name == "Helga Norman" or name == "Zach Conroy":
                print(f"There is an active arrest warrant on {name}.")
                name_loop = False
            elif name.isalpha():
                name_loop = False
                names.append(name)
            else:
                print("Names can only include alphabetical characters.")
        except ValueError:
            print("That is not a valid name, please enter a valid name: ")
    '''Start speed limit loop'''
    print("What is the speed limit in the area? ")
    s_limit_loop = True
    while s_limit_loop:
        try:
            speed_limit = int(input())
            if speed_limit <= 0:
                print(f"{speed_limit} is not a valid speed limit, please enter a valid speed limit.")
        except ValueError:
            ("That is not a valid speed limit, please enter a valid speed limit: ")
    
    
    