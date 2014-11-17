# CODE CHALLENGE: Solve the String Composition Problem.
#      Input: An integer k and a string Text.
#      Output: Compositionk(Text), where the k-mers are written in lexicographic order.
#
# Sample Input:
#      5
#      CAATCCAAC
#
# Sample Output:
#      AATCC
#      ATCCA
#      CAATC
#      CCAAC
#      TCCAA

from main.src.HelperFunctions.InOutHelper import *

fileName = 'rosalind_lexf'
fIn = open(getFullPathInput(fileName), 'r')
fOut = open(getFullPathOutput(fileName), 'w')

nt = fIn.readline().strip()
n = int(fIn.readline())

kmers = []
for i in range(0, len(nt)-n+1):
    kmers.append(nt[i:n+i])

for kmer in sorted(kmers):
    print(kmer)

fIn.close()
fOut.close()