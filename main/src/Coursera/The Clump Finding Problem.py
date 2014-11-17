from __future__ import print_function
from src.HelperFunctions.InOutHelper import *

fileName = 'input'
# fIn = open(getFullPathInput(fileName), 'r')
# text = fIn.readline().strip()

text = 'CCGACAGGCTAGTCTATAATCCTGAGGCGTTACCCCAATACCGTTTACCGTGGGATTTGCTACTACAACTCCTGAGCGCTACATGTACGAAACCATGTTATGTAT'
k = 4
L = 500000
t = 3

d = {}

for i in range(len(text) - k+1):
    kmer = text[i:k+i]
    if d.get(kmer) == None:
        d[kmer] = 1
    else:
        d[kmer] += 1
c = 0
for k, v in d.items():
    if v <= t:
        print(k, end=' ')
        c += 1
print(c)

# fIn.close()