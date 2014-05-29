fIn = open('rosalind_ini5.txt', 'r');
fOut = open('output.txt', 'w')
counter = 1
for line in fIn:
    if counter % 2 == 0:
        fOut.write(line)
    counter += 1
fIn.close()
fOut.close()