#===============================================================================
# 
# Problem
# 
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# 
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
# 
# Given: A DNA string t having length at most 1000 nt.
# 
# Return: The transcribed RNA string of t.
# 
# Sample Dataset
# 
# GATGGAACTTGACTACGTAAATT
# Sample Output
# 
# GAUGGAACUUGACUACGUAAAUU
#===============================================================================

from main.src.HelperFunctions.InOutHelper import *

fileName = 'rosalind_rna'
fIn = open(getFullPathInput(fileName), 'r')
fOut = open(getFullPathOutput(fileName), 'w')
s = fIn.readline()

ntDict = {ord('T'):'U'}
res = s.translate(ntDict)

fOut.write(res+'\n')
print(res)

fIn.close()
fOut.close()