# this script will count each email domain from the 
# empoyee.csv file
# Author: Nur Bujang
#

import csv
FILENAME = "employees.csv"
domainCount = {}

with open(FILENAME, "rt") as employeeFile:
    csvReader = csv.reader(employeeFile, delimiter = ',')
    firstLine = True
    count = 0 # to count the lines
    for line in csvReader:
        if firstLine:
            firstLine = False
            continue
        email = line[8]
        start = email.find('@')
        domain = email[start+1:]
        if domain not in domainCount:
            domainCount[domain] = 0
        else:
            domainCount[domain] += 1


for key, value in domainCount.items():
    print(key, "\t\t", value)

