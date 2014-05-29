# Problem
#
#
# Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.
#
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#
# Return: The Hamming distance dH(s,t).
#
# Sample Dataset
#
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# Sample Output
#
# 7

dirName = 'InOut\\'
fileName = 'input'
fIn = open(dirName + fileName + '.txt', 'r')
s = [fIn.readline().strip(), fIn.readline().strip()]
#s = ['GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT']

dH = 0
for pos, nt in enumerate(s[0]):
    if nt != s[1][pos]:
        dH += 1
print(dH)

fIn.close()