# Example for reading a file located
# In our local filesystem

NAME = "mynotes.txt"

# Open the file
myfile = open(NAME, 'r')

print("File openned: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

myfile.close()

f = open(NAME, 'a')
f.write('THIS IS A TEXT EXAMPLE TO ADDING TO MY FILE')
f.close()
print("The end")
