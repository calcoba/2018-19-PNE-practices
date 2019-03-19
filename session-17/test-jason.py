import json
import termcolor


# -- Open Json file
f = open("person.json", 'r')

# -- Read the data from the file
# -- Now person is a dictionary with all the information
person = json.load(f)

print()

termcolor.cprint("Name: ", 'green', end='')
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'green', end='')
print(person['age'])

for i, num in enumerate(person['phonenumber']):
    termcolor.cprint(" Phone {}:".format(i))

    termcolor.cprint("     Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("     Number: ", 'red', end='')
    print(num['number'])
