print("Welcome officer,\nPlease enter names to check for arrest warrants and calculate fines\nInput:")
code_loop = True
while code_loop:
    name_loop = True
    while name_loop:
        name = str(input())
        if name == "John Smith" or name == "Helga Norman" or name == "Zach Conroy":
            print(f"There is an active arrest warrant on {name}.")
            name_loop = False
        elif name.isalpha():
            name_loop = False
        else:
            print("Names can only include alphabetical characters")
            
    
    