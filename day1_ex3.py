# program that takes three or more words
# from the command line
# the program will then print out the words
# sorted in alphabetical order, with the last word
# preceed by the word 'and', and the first word
# capitalised

import sys

# takes elements from 1 to end of the line in the
# command line
word_list = sys.argv[1:]

# sort the list alphabetically, but first
# make sure everyone is lower case so that
# sort works as expected

word_list_lower = [w.lower() for w in word_list]

# now, sort the list
word_list_lower.sort()

# insert the the 'and' at position -2 (i.e. 
# second to last)
word_list_lower.insert(-1,'and')

#join the list elements into a string, separated by
# commas

output=(", ").join(word_list_lower[0:-1])

# print something to let the user know things are
# coming
print "Your list of words are:"

# capitalise the first word
print output.capitalize()+" "+word_list_lower[-1]+"."

print "All done!"

