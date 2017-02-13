#Lesson 1
#By Brian Lundell
#----------------------------------------INTRO----------------------------------------------------------
print "hello world"
#print is a the print function and will output all string text within the "" can also use ''

# "#" is the comment out command, it will leave off all code printed afterwards on the same line

#python operates line by line, whitespace/blank lines are skipped by python


#------------------------------------------MATH---------------------------------------------------------
#adding a comma after a print function with math operation will print out the resultant of the operation
print "Printing out 5+2", 5+2
print "Print 5*2", 5*2
# % is the remainder of diviion
print"Print R of 5/2", 5%2
# Division is dependent on data type 7/4 !== 7.0/4.0
print"Print the result", 7.0/4.0
#round(number) rounds a floating point number


#--------------------------------------VARIABLES------------------------------------------------------
#variables are created simply by adding a equal sign to a value
variable = 4.5
#you can subsitute something using %
print "variable = %s" %variable
# %s prints out a variable's value
# %d
# %r prints out an item no matter what, "prints out the garbage" //Good for debugging

#------------------------------------------------ADV STRINGS------------------------------------------
# we can assign variables as strings
stringVar = "Hey Guys what's %s" %7
print stringVar
#You can combine strings with +. It adds it directly to the end of the other string
otherStringVar = " It's 7 dude"
print stringVar + otherStringVar
#Strings can be printed multiple times using the * operator
print stringVar*2
#you can use () to print of multiple variables
print (stringVar, otherStringVar) #You can use this to go
print "What is %s divided by %s " %(4, 2),2
#We can divide text across lines like so
print stringVar,
print otherStringVar

#---------------------------------------------MORE Printing-------------------------------------------
#Variables like this to multi functional
Formatter = "%r %r %r %r"
print Formatter % (1, 2, 3, 4) + " I luv numbers"
# \n prints an item afterwards onto a new lines
print "Hey! \nDown Here!"
# \ forward slash is the break command for python strings, If you needed to include quotations \" or ' or \, place a \ in front
#\t is the tab operator, it will insert a tab
print "Hey World \t Over Here!"
#Using triple quotes """ or ''' for strings will print out all '," in a string
print """ Hey I'll use all the quotes'a'"""

#----------------------------------------------Taking Inputs-------------------------------------------
#You can take raw variables by variableName = raw_input(), this automatically assigns the variable the correct datatype
print "Enter age and name",
ageVar = raw_input()
nameVar = raw_input()
print "HEY %s %s" % (ageVar,nameVar)
#int() is a function that converts anything into an integer. Ex it can convert a string into a interger
#input() apparently has security issues, avoid it
#putting text inside the () of the raw_input function will prompt the user with it
newNameVar = raw_input("Name? ")
print newNameVar
