#Lesson 3
#By Brian Lundell
#-------------------------------MORE READING AND Writing-----------------------------------------------------
#from sys import argv
#from os.path import exists
# exists is a true or false statement that will execute when set to true

#--------------------------------------------FUNCTIONS-------------------------------------------------------------
#to define a function the syntax is def functionName(arg,arg,etc):
#                                       function process
#Items indented will be included in the function
#No such thing as void, int, double to notify return types
def PrintMe(arg1, arg2):
    print "Hey it's %r and %r" % (arg1, arg2)

def addFun(arg1, arg2):
        #sum = arg1 + arg2
        return arg1+arg2


Varg1 = raw_input("Enter name > ")
Varg2 = raw_input("Enter name again > ")
PrintMe(Varg1, Varg2)


#-----------------------------------------Returning Data From a Function-----------------------------------------------
#raw_input() read this data as a string, using input() converts it into a digit
Narg1 = input("Enter Data > ")
Narg2 = input("Enter Data > ")

data = addFun(Narg1, Narg2)
print data

#---------------------------------------------BOOLEAN-------------------------------------------------------------
# and, or, not || and returns true when both are true, or returns true when at least one is true, not flips an item's boolean status
# Tests are !=, ==, >=, <=, >, <
#True and False boolean expressions too, you assign a variable this status and use them to test things
#if-statements are constructed like FUNCTIONS

a = 1
b = 2
c = 3
if a > b:
    print "WRONG"
if c > b:
    print "RIGHT"

#Else and Elif
if a == b:
    print "WRONG"
else:
    print"ALSO RIGHT"
#Else is paired with an if statement and automatically runs if the if statement fails.
#Elif is else if in C++. do not write else if, just Elif
