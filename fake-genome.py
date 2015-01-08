import random

dna = list('ACGT')
dna = dna * 250
random.shuffle(dna)

print '>genome'
print ''.join(dna)
