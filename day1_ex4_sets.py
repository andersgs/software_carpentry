# given a string, which is a sentence
# find how many letters A-Z that sentence 
# contains. capital and lower case should
# not be counted

# take two sentences, and find how many letters
# they have in common, and hwo many are unique
# to each sentence

import sys,re

sentence = sys.argv[1:]

if len(sentence) == 1:
    print "Your sentence has the following number of unique letters:"
    
    #set sentence
    new_sent = sentence[0]
    
    #first lower case all the sentence
    new_sent = new_sent.lower()
    
    #strip non alpha characters from the sentence
    new_sent = re.sub('[\W_]+','',new_sent)
    
    #output total unique characters
    result = set(new_sent)
    print len(result)
    #return len(set(new_sent))

elif len(sentence) == 2:
    
    #unfold the list of sentences to individual sentences
    sent1 = sentence[0]
    sent1 = re.sub('[\W_]+','',sent1)
    sent2 = sentence[1]
    sent2 = re.sub('[\W_]+','',sent2)
    
    #find individual sets
    set1 = set(sent1)
    set2 = set(sent2)
    
    #print some output
    print "Total unique characters for sentence 1: {}.".format(len(set1))
    print "Total unique characters for sentence 2: {}.".format(len(set2))
    
    print "Total of shared characters for sentences 1 and 2: {}.".format(len(set1.intersection(set2)))
    
    print "The unique letters for sentence 1: {}.".format(len(set1.difference(set2)))
    
    print "The unique letters for sentence 2: {}.".format(len(set2.difference(set1)))

else:
    print "Number of sentences is not 1 or 2"
