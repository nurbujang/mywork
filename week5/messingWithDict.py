# messingWithDict.py
# Messing with dictionaries
# Author: Nur Bujang

# i want to store details about a car

car = {
    "make" : "ford",
    "model" : "modeo",
    "year"  : 2006,
    "owner" : {
        "name" : "andrew",
        "driver-number": 1123
    }
}


print(car["year"])
print(car["owner"]["name"])
print (type(car["owner"].get("names")))
