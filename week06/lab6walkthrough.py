# lab6walkthrough.py
# 
# Author: Nur Bujang

# Program that Andrew wrote during the walk through video


students = []
def displayMenu():
    print("menu")
    print("\t(a) add")
    print("\t(v) view")
    print("\t(q) quit")
    choice = input("please select (a/v/q):")
    return choice

def getModules():
    modules = []
    modulename = input ("please enter the module name (blank to quit)")
    while (modulename != ""): # If it's not equal to blank, Then I need to make a module with that module name
        module = {} #so i make the module which is a blank object
        module["name"] = modulename # the name is equal to whatever that's read in
        module["grade"] = int(input("enter grade")) # the grade turned into an integer, if no grade, error
        modules.append(module) # append that into modules
#check to see if they want another module, get the next module name, continue sentinel controlled while loop
        modulename = input("please enter the module name (blank to quit)") 

    return modules # keep appending modules into module, and when finished, return module

def doAdd(students):
    student ={}
    student["name"] = input("please enter name:")
    student["modules"] = getModules()
    students.append(student)

    
def doView(students):
    for student in students: # iterate through that list
        print (student["name"])
        for module in student["modules"]: # for each of the modules, 
            print ("\t", module["name"], "\t:", module["grade"])

choice = displayMenu()
while choice != "q":
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    else:
        print ("invalid choice")


    choice = displayMenu()

print ("goodbye")
