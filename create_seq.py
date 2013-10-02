import sys
from nucleotide_seq import NucleotideSequence, DNASequence, RNASequence

def get_seq():
    tries = 0
    while True:
        seq = raw_input("Please enter a DNA or RNA sequence: ")
        try:
            res = DNASequence(seq)
            return res
        except:
            try:
                res = RNASequence(seq)
                return res
            except:
                tries += 1
                if tries > 4:
                    print '''
                    Sorry, I could not use any of the tried sequences.
                    DNA sequences should only include: A, T, C and G
                    RNA sequences should only include: A, U, C and G
                    
                    I am exiting now!
                    '''
                    raise
                print "Sequence was not valid. Please try again."
                print "You have {} more tries.".format(5-tries)
                print ""
                

if __name__=='__main__':
    sequence = get_seq()
    print "The input sequence is {}.".format(sequence.seq)
