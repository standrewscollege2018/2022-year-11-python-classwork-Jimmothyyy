import sqlite3
DATABASE = 'Cars.db'
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()
cursor.execute("SELECT * FROM car")
results = cursor.fetchall()

for entry in results:
    print (f"{entry[0]:2} {entry[4]:12} {entry[5]:15}")
input_loop = True
while input_loop:
    try:
        query = int(input("Please enter the ID of the car you want to search: "))
        if query <= 10 and query >= 1:
            input_loop = False 
        else:
            print("That is not a valid ID, please enter a valid ID: ")
    except ValueError:
        print("That is not a valid ID, please enter a valid ID: ")
cursor.execute("SELECT * FROM car WHERE car_ID = ?", (query,))
results = cursor.fetchall()
print (f"{'ID:':3} {'Licence:':10} {'Colour:':11} {'Driver:':16} {'Make:':13} {'Model:':16}")
for entry in results:
    print (f"{entry[0]:3} {entry[1]:10} {entry[2]:11} {entry[3]:16} {entry[4]:13} {entry[5]:16}")


