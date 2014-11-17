from __future__ import print_function
from src.HelperFunctions.InOutHelper import *

# fileName = 'input'
# fIn = open(getFullPathInput(fileName), 'r')
# text = fIn.readline().strip()

text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
count = 0

def frequentwords(text, k):
    FP = []
    c = []
    for i in range(0, len(text) - k):
        pattern = text[i:i+k]
        c.append(countwords(text, pattern))
    maxC = max(c)
    for i in range(0, len(text) - k):
        if c[i] == maxC:
            if text[i:i+k] not in FP:
                FP.append(text[i:i+k])
    return FP


def countwords(text, pattern):
    count = 0
    lenPattern = len(pattern)
    for i in range(len(text) - lenPattern+1):
        if text[i:lenPattern+i] == pattern:
            count += 1
    return count

pattern = frequentwords(text, k)[0]
print (pattern)

for i in range(0, len(text) - len(pattern)+1):
    pt = text[i:i+len(pattern)]
    c = 0
    for j in range(0, len(pt)):
        if pattern[j] != pt[j]:
            c += 1
    if c<=d:
        count += 1
        print(pt, end=' ')
        # print (i, end=' ')
print (count)

# fIn.close()