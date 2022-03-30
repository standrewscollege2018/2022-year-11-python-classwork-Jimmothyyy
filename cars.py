import sqlite3
DATABASE = 'Cars.db'
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

search_parameters = ["ID", "Licence plate", "Colour", "Driver", "Make", "Model"]
i = 1

print (f"Which field would you like to search in?")
for field in search_parameters:
    print (f"{i}. {field}")
    i += 1
search = int(input())
if i = 1
elif i = 2
elif i = 3
elif i = 4
elif i = 5
elif i = 6
