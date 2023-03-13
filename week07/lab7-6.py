students= []
def displayMenu():
    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("type one letter (a/v/s/q):").strip()
    return choice

def doAdd(students):
    # you have code here to add
    print("in adding")
def doView(students):
    # you have code here to view
    print("in viewing")
def saveDict(students):
    print("save dict")
def doSave(students):
    saveDict(students)#you will put the call to save dict here
    print("in save")
def writeDict(students):
    print("students saved")

#main program
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice !='q':
        print("\n\nPlease select either a,v,s or q")
    choice=displayMenu()