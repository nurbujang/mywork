# Messing with csv
# This is program is to demonstrate 
# storing data in a CSV format
#
# Author: Nur Bujang

import csv
FILENAME="data.csv"
with open(FILENAME, "rt") as file:
    csvReader = csv.reader(file, delimiter = ',') # delimiter can be anything, in this case a comma
    for line in csvReader: # line will be a list containing the variables in each line
        age = line[2]   # the age
        print(age)      # note this is printing the header row, I provide a solution to this in the tutorial
mydict =[{'first': 'Andrew', 'last': 'Beatty', 'age':'2'},
         {'first': 'joe', 'last': 'Bloggs', 'age':'22'},
         {'first': 'Mary', 'last': 'mc', 'age':'2222'} 
        ] 
    
# field names 
fields = ['first', 'last', 'age'] 
    
# name of csv file 
FILENAME = "data.csv"
    
# writing to csv file 
with open(FILENAME, 'w', newline='') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
    for dictrow in mydict:
        print(dictrow)
        writer.writerow(dictrow) 