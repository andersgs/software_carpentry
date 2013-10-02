#I'll mess with your code Brasileiro!
from string import maketrans
class DNAsequence:
    def __init__(self,sequence):
        self.seq = sequence
        self.base_counts = {}
        self.len = 0
    def seq_len(self):
        if self.len == 0:
            self.len = len(self.seq)
            return self.len
        else:
            return self.len
    def base_count(self,base):
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            counts = self.seq.count(base)
            self.base_counts[base] = counts
            return counts
    def gc_content(self):
        return (self.base_count('C') + self.base_count('G')) * 100.0 / self.seq_len()
    def reverse_complement(self):
        intab = 'ATCG'
        outtab = 'TAGC'
        transtab = maketrans(intab,outtab)
        rev = self.seq[::-1]
        return rev.translate(transtab)

test = DNAsequence("ATCG")

print test.seq_len
print test.base_count('C')
print test.gc_content()
print test.reverse_complement()
