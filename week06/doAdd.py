# doAdd.py
# 4. So we need to think what we want this to do.
# a. Read in the student’s name (that is straightforward)
# b. Read in the module names and grades (this is a bit more complicated
# so let’s put this in separate function and think about it by itself, see 5. below)
# c. Test this function, it creates a student dict, we can print that out.
# d. We should add the student dict to list (pass this list in)
# e. Test this.
# Note: I have put this in a separate file, 
# I am not thinking about the menu at the moment, I just what to see if I can read in a student
# Author: Nur Bujang


def readModules():
    return []


def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)


#test
students = []
doAdd(students)
doAdd(students)
print (students)
