#Lesson 2
#By Brian Lundell
#----------------------------------------------SYSTEM ARGUMENTS----------------------------------------
from sys import argv
#from command tells us to take a module/library and take something from it
#import
#from/import only takes a certain subset from the library to be included in our code
#keeps it smaller and simple
script, one = argv
print script, one
#in the command line "python filename.py argument"
#The script = filename.py, one = argument and so on

#-----------------------------------------------Reading & Writing Files---------------------------------------------
#We can open files using arguments from the terminal
#using the import arg above, we can load a test doc such as testdoc
#The open() function will open a file within the same location and store the contents into the variable
#using the .read() function will read the file and using it with print command will print it off

#open(filename,permission) choosing the permissions lets write, read, append something
# "r+" allows for reading and Writing, adds in writing in front of file
# "a+" allows for reading and appending, adds in wriitng at end of file and creates the file if it does not exist
# "w+" allows for just wriitng and will truncate all other items
# the default for open() is read only and + for the permissions opens it in read and write
testfile = open(one,"a+")
print testfile.read()
# open() opens a function
# close() will save and close a file
# .read() reads the entire file
# .readline() reads the file line by line
# .truncate() will clear the entire file
# .write(stuff) will write stuff into the file
myString = "BRIANBRIANBRIANBRIANBRIAN"
testfile.write("\n")
testfile.write(myString)
print testfile.read()
testfile.close()
