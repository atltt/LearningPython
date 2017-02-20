#Lesson 4
#By Brian Lundell
#----------------------------------------------------Lists------------------------------
#Lists basically the same as arrays. Arrays do exist in python but they are data specific  They use [] instead of {}
#You can mix data types in lists
varList = [1,2,3,4]
varList2 = [] #This creates an empty list
varList3 = [1,'apples', 'oranges', 4]


#----------------------------------------FOR-LOOPS & LIST----------------------------------------
#For loops are created using the same type of function declaration
for number in varList:
    print "Look at this %d" % number
    #This will print off anything within the range of the list until it reaches a maximum
for fruit in varList3:
    print "What is this %r?" %fruit

#Fruit, Number, and i all act as a iterator for our for loops


varList4 = []

for i in range(0,6):
#This format creates the range 0-5, giving a total of six of spaces
    varList4.append(i)
    #.append is a list function that will add that item at the end of the list
    # append can also be called as append(varlist4,elemet)
    #since the range is 0-6 we can access 0-5 index spots
    # .insert(index, element) this will put the element at index index
    # .extend(element) will extend the current list and add the element at the end of the
    # .index(element) will return the index where the element exists at
    # .remove(element) will remove the element from the list
    # .sort() and .reverse() will will sort and reverse the list
    # .pop() will return all elements of the list
for i in varList4:
    print "Number is equal to %d" % i
for i in range(0,4): #This is how you set bounds for the for loop
    print varList4[i]
    #This will access the element at index i

#-----------------------------------------WHILE LOOPS----------------------------------------------
#While looos will run until the boolean expression is no longer true
#These lead to infinite loops often
i=0
while i<5:
    print varList4[i]
    i+=1
#This works the same as the for loop above but it needs more lines of code

#-----------------------------------------------BRANCHES-------------------------------------------
#Branches nest items within each of each other
#Indentations matters a ton when branching
def thisFunc(arg1, arg2):
    if arg1 > arg2:
        print arg1, arg2
    else:
        if arg2 > arg1:
            print arg2, arg1
        elif arg1 == arg2:
            print "arg1 is arg2"


data1 = raw_input("> ")
data2 = raw_input("> ")
thisFunc(data1, data2)

#------------------------------------------------------------Exit(0) & List-------------------------------------------
#exit(0) is a function that will end the current program
# https://learnpythonthehardway.org/book/ex37.html
#This is a repo of the list of useful commands we need to learn.

#SPLICE
#Using varList4[2:4] is slicing a list
#This will include on the item(s) between 1 and 3
print varList[1:4]

#----------------------------------------------------------DICT Function-----------------------------------
#You can associate terms with others.
#You can only call terms on the left hand side
#Must use {} to create a dictionary
varList5 = {'one': 'Two', 4: 'alpha', 'beta': 'Omega'}
print varList5['one']
print varList5[4]
print varList5['beta']

# .get(index) will get the element/association at this index
print varList5.get('one')

del varList5['beta']
#print varList5['beta'] will return an error since the association was deleted in the previous line

varList6 = {'TN': 'Tennessee', 'FL': 'Trash', 'CA': 'California'}

# .items() brings up the entire list of the list
#This for loop has two iterators will atoumatically assign itself to abrevs = TN and state =  Tennessee
for abrevs, state in varList6.items():
    print "%s is %s" % (abrevs, state)
