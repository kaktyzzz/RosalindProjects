#===============================================================================
# Problem
# 
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# 
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# 
# Given: A DNA string s of length at most 1000 bp.
# 
# Return: The reverse complement sc of s.
# 
# Sample Dataset
# 
# AAAACCCGGT
# Sample Output
# 
# ACCGGGTTTT
#===============================================================================
from main.src.HelperFunctions.InOutHelper import *

fileName = 'rosalind_revc'
fIn = open(getFullPathInput(fileName), 'r')
fOut = open(getFullPathOutput(fileName), 'w')
#s = fIn.readline().strip()
s = 'AAAACCCGGT'

ntType = ['A', 'C', 'G', 'T']
complDict = dict(zip(ntType, ntType[::-1]))

#complDict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
result = ''.join(complDict[nt] for nt in s[::-1])
 
print(result)
fOut.write(result+'\n')
      
fIn.close()
fOut.close()