# take an input sequence and create a dictionary containing base counts

import sys

# the test sequence has 3 bases for each of the valid bases (A,T,C,G)
dna_sequence = "AAATTTGGGCCC"

rna_sequence = 'AAAUUUGGGCCC'

#valid dna bases
dna_val = set(['A','T','C','G'])

rna_val = set(['A','U','C','G'])

#first step, make sure they are upper case, and valid

seq_up = rna_sequence.upper()

#check if valid

if set(seq_up)==dna_val:
    print "Sequence OK, and it seems to be DNA."
    dic = {k:seq_up.count(k) for k in ['A','T','C','G']}
elif set(seq_up)==rna_val:
    print "Sequence OK, and it seems to be RNA."
    dic = {k:seq_up.count(k) for k in ['A','U','C','G']}
else:
    print "Sequence has unknown characters"
    sys.exit()

print dic

#doing GC% content
n_bases = len(seq_up)

n_gc = dic['C'] + dic['G']

print "The GC content is {}%.".format(float(n_gc)*100/n_bases)
