"""
Write some python code that checks if a given number (entered from the 
command line) is odd or even.  
The script accepts a single integer parameter and checks if it's an even or
 odd number.  If even, it prints "Even" and if odd, it prints "Odd".
"""

import sys

#exercise 1 for ifelse
numb = int(sys.argv[1])

if numb%2 == 0:
    res1 = 'Even'
else:
    res1 = 'Odd'

#exercise 2 for ifelse
if numb > 0 and numb < 50:
    res2 = 'Minor'
elif numb >= 50 and numb < 1000:
    res2 = 'Major'
else:
    res2 = 'Severe'
    
print 'The number is both {} and {}.'.format(res1,res2)

#exercise 3 for ifelse
scores = [85.0,75.0,95.0,110.0,56.0]

total = 0.0
for score in scores:
    total += score

print "The total for the scores {} is {}.".format(scores,total)

#another way of doing the sum
total = 0.0
total = reduce(lambda x,y: x+y,scores)

print "Using reduce and lambda, the total score is {}.".format(total)
