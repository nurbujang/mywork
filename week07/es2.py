FILENAME="moby-dick.txt"
with open(FILENAME, 'r') as f:
    data = f.read()
    
# start AFTER "WHALE SONG."
start_content = data.split('CHAPTER 1') 

# declare ending_text, end BEFORE "End of this Project Gutenberg etext of Moby Dick, by Herman Melville"
ending_text = 'End of this Project Gutenberg etext of Moby Dick, by Herman Melville'

import argparse

#create an argument object
parser = argparse.ArgumentParser() 

# make calls to the add_argument() method
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

# call the argument 'filename'
parser.add_argument('filename')

# parse the argument(s)
args = parser.parse_args()


# access the 'filename' argument
#print(args.filename)

filename = args.filename
