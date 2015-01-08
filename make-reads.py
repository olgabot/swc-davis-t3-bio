import sys
import screed
import random

# Number of reads
N = 1000

# Sequence length
L = 100

genomefile = sys.argv[1]

# Even though our genome file only has one sequence, this is
# a hack around this so we open the file, and we get the last
# sequence, which in this case is our one sequence
for record in screed.open(genomefile):
    genome = record.sequence

for i in range(N):
    start = random.randint(0, len(genome) - L - 1)
    end = start + L
    read = genome[start:end]

    if random.choice([0, 1]):
        read = screed.rc(read)
        
    assert len(read) == L
    print '>read{0:03d}\n{1}'.format(i, read)
