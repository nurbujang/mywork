# testTypes.py
# Author: Nur Bujang
# Lab 3.1 Variables and State

# to create 5 variables, one for each of the following types
## int
## float
## boolean
## str
## list
i=3
fl=3.5
isa=True
memo='how now Brown Cow'
lots=[]

# Use the type () function to check that the variables are of that type
print('variable {} is of type:{} and value:{}'.format('i',type(i),i))
print('variable {} is of type:{} and value:{}'.format('fl',type(fl),fl))
print('variable {} is of type:{} and value:{}'.format('isa',type(isa),isa))
print('variable {} is of type:{} and value:{}'.format('memo',type(memo),memo))
print('variable {} is of type:{} and value:{}'.format('lots',type(lots),lots))

# 'lots' is a string under the class 'list', not the variable lots
# so output became: variable lots is of type:<class 'list'> and value:[]

# lots is the variable lots