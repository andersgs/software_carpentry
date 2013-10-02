from string import maketrans

class InvalidBaseException(Exception):
    pass

class NucleotideSequence:
    '''A general nucleotide class. The class is inherited by DNASequence
    and RNASequence classes. Not for general use. Use DNASequence and
    RNASequence instead.'''
    intab = 'ATCG'
    outtab = 'TAGC'
    transtab = maketrans(intab,outtab)
    valid = set(intab)
    def __init__(self,sequence):
        '''Takes a string of nucleotides in upper case.
        For example: 'ATCGGGAA' for DNA or 'AUCGGGUU' for RNA.
        '''
        assert isinstance(sequence,str)
        assert len(sequence) > 0
        if set(sequence).difference(self.valid) != set():
            raise InvalidSequenceException("Invalid base(s) in the sequence: {}".format(set(sequence).difference(self.valid)))
                #raise

        self.seq = sequence
        self.base_counts = {}
        self.len = 0
    def seq_len(self):
        '''Return the length of the nucleotide sequence.'''
        if self.len == 0:
            self.len = len(self.seq)
            return self.len
        else:
            return self.len
    def base_count(self,base):
        '''Given a base <base> return the count of that base in the nucleotide sequence.'''
        assert isinstance(base,str)
        assert len(base) == 1
        assert base in self.valid
        
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            counts = self.seq.count(base)
            self.base_counts[base] = counts
            return counts
    def gc_content(self):
        '''Return the GC% (0 to 100%) content in the nucleotide sequence.'''
        return (self.base_count('C') + self.base_count('G')) * 100.0 / self.seq_len()
    def reverse_complement(self):
        '''Return the reverse-complement of the nucleotide sequence.'''
        rev = self.seq[::-1]
        return rev.translate(self.transtab)

class DNASequence(NucleotideSequence):
    '''Class appropriate for DNA sequences. Assumes only A,T,C and G are found in the sequence.'''
    pass

class RNASequence(NucleotideSequence):
    '''Class appropriate for RNA sequences. Assumes only A, U, C and G are found in the sequence'''
    intab = 'AUCG'
    outtab = 'UAGC'
    transtab = maketrans(intab,outtab)
    valid = set(intab)

if __name__=='__main__':

    test = DNASequence("ATCG")
    test2 = RNASequence("AUCG")

    print test.seq_len()
    print test.base_count('C')
    print test.gc_content()
    print test.reverse_complement()
    
    print test2.seq_len()
    print test2.base_count('C')
    print test2.gc_content()
    print test2.reverse_complement()
