#  Sample Input:
#
# ACCGA
# CCGAA
# CGAAG
# GAAGC
# AAGCT
#
# Sample Output:
#
# ACCGAAGCT
from main.src.HelperFunctions.InOutHelper import *

fileName = 'rosalind_lexf'
fIn = open(getFullPathInput(fileName), 'r')
fOut = open(getFullPathOutput(fileName), 'w')


dna = ''
for line in fIn.readlines():
    line = line.strip()
    if dna == '':
        dna += line
    else:
        dna += line[-1:]

print(dna)

fIn.close()
fOut.close()