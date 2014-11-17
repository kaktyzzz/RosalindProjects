from __future__ import print_function
from src.HelperFunctions.InOutHelper import *

# fileName = 'input'
# fIn = open(getFullPathInput(fileName), 'r')
# text = fIn.readline().strip()

pattern = 'TGGCT'
text = 'AGGAAGCGCATGCGAACCGTGCAAATTCATGTGCTTTGGTCTAAGTTGCGTGCGTCTGACAAACTGTAATGAGAATCCTGTGCCTCCGCACTGGGGGGCAATGGAATGGGAACCCCTCGTGGCGGGAACGGACATGATCGTCTAACGGAAGCTACTTTCAAGCGCATTTACGAGTGGTTGCCACCATCAACGTCAGGACGATAGTGGTGCATACAACAGAAATGCGGCATGGATCGAAGCACCTTAGTTACCCTAGGATGTTCGTTTAACTCCCGCATTCTGGTGGCTAGCAGTCCCATTTCCGGCCTTACGCATACATACCGATATCAGAGCTCTATGTCCTAGGGGCTAATCCCACTAAGTGCTGGTGGTGTTAACTCCGCTGATAACTCT'
d = 3
count = 0

for i in range(0, len(text) - len(pattern)+1):
    pt = text[i:i+len(pattern)]
    c = 0
    for j in range(0, len(pt)):
        if pattern[j] != pt[j]:
            c += 1
    if c<=d:
        count += 1
        # print (i, end=' ')
print (count)

# fIn.close()