from  main.src.HelperFunctions.InOutHelper import *

fileName = 'rosalind_ini5'

fIn = open(getFullPathInput(fileName), 'r')
fOut = open(getFullPathOutput(fileName), 'w')
counter = 1
for line in fIn:
    if counter % 2 == 0:
        fOut.write(line)
    counter += 1
fIn.close()
fOut.close()