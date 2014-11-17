from __future__ import print_function
from src.HelperFunctions.InOutHelper import *

# fileName = 'input'
# fIn = open(getFullPathInput(fileName), 'r')
# text = fIn.readline().strip()

text = 'GATACACTTCCCAGTAGGTACTG'

lst = []
skew = 0
for k in text:
    if k == 'G':
        skew += 1
    if k == 'C':
        skew -= 1
    lst.append(skew)

m = min(lst)

indices = [i for i, x in enumerate(lst) if x == m]

for k in indices:
    print(k+1, end=' ')

# fIn.close()