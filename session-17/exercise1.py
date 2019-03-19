import json
import termcolor


# -- Open Json file
f = open("persons.json", 'r')

# -- Read the data from the file
# -- Now person is a dictionary with all the information
persons = json.load(f)

print("Total people in the database: {}".format(len(persons['List of persons'])))
print()
for person in persons["List of persons"]:
    termcolor.cprint("Name: ", 'green', end='')
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end='')
    print(person['age'])
    termcolor.cprint("Phone numbers: {}".format(len(person['phoneNumber'])), 'green')

    for i, num in enumerate(person['phoneNumber']):
        termcolor.cprint(" Phone {}:".format(i), 'blue')

        termcolor.cprint("     Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("     Number: ", 'red', end='')
        print(num['number'])
    print()
