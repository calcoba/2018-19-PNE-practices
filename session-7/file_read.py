# Example for reading a file located
# In our local filesystem

NAME = "mynotes.txt"

# Open the file
myfile = open(NAME, 'r')

print("File openned: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

myfile.close()
