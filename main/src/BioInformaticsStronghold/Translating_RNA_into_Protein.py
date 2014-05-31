# Problem
#
# The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.
#
# The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.
#
# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#
# Return: The protein string encoded by s.
#
# Sample Dataset
#
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# Sample Output
#
# MAMAPRTEINSTRING

from main.src.HelperFunctions.InOutHelper import *
from main.src.HelperFunctions.BioHelper import *

fileName = 'input'
fIn = open(getFullPathInput(fileName), 'r')
fOut = open(getFullPathOutput(fileName), 'w')

rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
#rna = fIn.readline().strip()
codonDict = getRNACodonTable()
for i, c in enumerate(rna):
    codon = ''
    codon += c
    if ((i+1) % 3 != 0):

        print(i)
    else:
        print(codon)
        if codon in codonDict:
            fOut.write(codonDict[codon])
        else:
            print('Error')
        codon = ''

fIn.close()
fOut.close()