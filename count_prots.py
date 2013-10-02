# count how many human proteins there are in swissprot FASTA file

import sys,re

# a function to help in updating the screen with information to the user
def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()

#check if the line is a FASTA identifier line, and if so, if the sequence
# belongs to Homo sapiens

def is_human_prot(line):
    if line[0] == '>':
        if re.search('os=homo sapiens',line.lower()):
            return 1
        else:
            return 0
    else:
        return 0

#get the filename
filename = sys.argv[1]

#open the file to read
f = open(filename,'r')

# initialise our counter variables
total_count = 0
count_lines = 0

#loop over the lines while outputting some information to the user every 1000
# lines
for line in f:
    #check if the line intialises a new sequence record (i.e., must start with
    # a '>'. if so, add to count_lines counter
    if line[0] == '>':
        count_lines += 1
        total_count+=is_human_prot(line.strip())
    #send some output to the screen to keep the user entertained.
    if count_lines%1000 == 0:
        restart_line()
        sys.stdout.write('\rTotal proteins examined so far {}, and total human proteins found {}.'.format(count_lines,total_count))
        sys.stdout.flush()
print ""
print "Done."
print "Total number of Homo sapiens proteins in the file {} is {} out of a total {}.".format(filename,total_count,count_lines)
