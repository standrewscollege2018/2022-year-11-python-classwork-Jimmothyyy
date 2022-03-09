'''Set variables'''
bypass_loop = True
end_code = False
booked_cars = 0
'''Define lists'''
cars_rental_list = [["Suzuki Van", "(2)", True],
                    ["Toyota Corolla", "(4)", True],
                    ["Honda CRV", "(4)", True],
                    ["Suzuki Swift", "(4)", True],
                    ["Mitsubishi Airtrek", "(4)", True],
                    ["Nissan DC Ute", "(4)", True],
                    ["Toyota Previa", "(7)", True],
                    ["Toyota Hi Ace", "(12)", True],
                    ["Toyota Hi Ace", "(12)", True]]
'''Begin run loop'''
run = True
while run:
    '''Check if all car have been booked'''
    if booked_cars == 9:
        rental_input = False
        bypass_loop = False
        run = False                    
        print("All cars have been booked for today.")    
        break
    bypass_loop = True
    print("Hello and welcome to Aperture Science's car rental program!")
    print("Here are a list of available cars: ")
    '''Fetch car name, seat number and availablility'''
    for car in cars_rental_list:
        if car[2] == False:
            print(car[0], car[1],", Unavailable")
        else:
            print(car[0], car[1])    
    '''Get rental input'''
    rental_input = True
    while rental_input:
        try:
            i = int(input("Which car would you like to book? (Press 0 to end rental day) "))          
            if i < 0 or i > 9:
                print("Not a valid input, please enter an integer between 1 and 9.")
            elif i == 0:
                if booked_cars >= 1:
                    rental_input = False
                    bypass_loop = False
                    run = False
                elif booked_cars == 0:
                    rental_input = False
                    bypass_loop = False
                    run = False                    
                    print("No cars have been booked today. ")
                    end_code = True
            elif cars_rental_list[i-1][2] == False:
                print(f"The {cars_rental_list[i-1][0]} is currently booked.")     
            elif cars_rental_list[i-1][2] == True:
                rental_input = False
        except ValueError:
            print("That is not a valid integer between 0 - 9")
    '''Assign availability status'''
    while bypass_loop:
        cars_rental_list[i-1][2] = False
        print(f"You have booked the {cars_rental_list[i-1][0]}.")
        booked_cars += 1
        name_loop = True
        while name_loop:
            name = input("What is your name? ")
            if len(name.replace(" ", "")) == 0:
                print("No name entered, please enter a name.")
            else:
                name_loop = False
                cars_rental_list[i-1].append(name.title())
        print(f"Thanks, {name.title()}.")
        bypass_loop = False
'''Daily summary'''
if end_code == False:
    print("Daily summary: ")
    for car in cars_rental_list:
        if car[2] == False:
            print (car[0], car[3])

        
            
        
