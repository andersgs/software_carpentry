# exercise 2 for functions

def base_count(seq,base):
    return seq.count(base)
    
def gc_content(seq):
    countC = base_count(seq,'C')
    countG = base_count(seq,'G')
    countTotal = len(seq)
    return (countC + countG) * 100.0 / countTotal
    
seq_test = 'AAATTCCCCGGGGG'

print base_count(seq_test,'A') #3
print base_count(seq_test,'T') #2
print base_count(seq_test,'C') #4
print base_count(seq_test,'G') #5

print gc_content(seq_test) # 9/14
