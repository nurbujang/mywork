# messing with files 
# Author: Nur Bujang

FILENAME= "data.txt" # put FILENAME in caps bc u want it to be constant, they dont change
'''
with open(FILENAME, 'rt') as f:
    for data in f:
        #print(data , end="" )
        print(data.strip() )
        #print(data[:-1])
'''
with open("data2.txt", "w+") as f:
    f.write("what the hell\n")
    f.write("brown cow\n")
    f.seek(0)
    data = f.read()
    print(data)

print("done")
    
