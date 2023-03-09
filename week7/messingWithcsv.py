# testing reading a csv
# author Nur Bujang

import csv

FILENAME = "test.csv"

with open(FILENAME, "rt") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    firstLine = True
    for line in csvReader:
        if firstLine:
            firstLine = False
            continue
        print (line[2])

# testing the right code to get email domains
# mess around to find the right code here
email = "qwerty@QWERT.ie"
print (email.find('@'))
start = email.find('@')
print (email[start+1:])