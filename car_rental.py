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
    print("Hello and welcome to Aperture Science's car rental program!")
    print("Here are a list of available cars: ")
    '''Fetch car name, seat number and availablility'''
    for car in cars_rental_list:
        if car[2] == False:
            print(f"{car[0], car[1]}, Unavailable")
        else:
            print(car[0], car[1])    
    '''Get rental input'''
    i = int(input("Which car would you like to book? "))
    '''Assign unavailable status'''
    cars_rental_list[i-1][2] = False

            
        
            
        
