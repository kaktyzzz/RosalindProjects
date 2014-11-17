# Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
#      Input: An amino acid string Peptide.
#      Output: Cyclospectrum(Peptide).
#
# CODE CHALLENGE: Solve the Generating Theoretical Spectrum Problem.
#
# Sample Input:
#      LEQN
#
# Sample Output:
#      0 113 114 128 129 227 242 242 257 355 356 370 371 484

from main.src.HelperFunctions.InOutHelper import *
from main.src.HelperFunctions.BioHelper import *


# fileName = 'rosalind_prot'
# fIn = open(getFullPathInput(fileName), 'r')
# fOut = open(getFullPathOutput(fileName), 'w')


pept = 'SEWETCTWRHSDVG'
# rna = fIn.readline().strip()

peps = []

peps.append('')
for i in range(1, len(pept)):
    for j in range(0, len(pept)):
        lst = pept[j:] + pept[:j]
        peps.append(lst[0:i])
peps.append(pept)

print(peps)
mass = []
for p in peps:
    mass.append(getMassPeptides(p))

print(mass)
for m in sorted(mass):
    print(m, end = ' ')