# # readModules.py
# # 5. We can now think about how to read in the modules. 
# # We want to keep reading modules until the user enters a module name of blank. 
# Doesn’t the data structure look ugly, and hard to read. 
# Maybe I should have done the function to view it before the function to add new ones!!
# # Author: Nur Bujang


def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()

    return modules


def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)


#test
students = []
doAdd(students)
doAdd(students)
print (students)
