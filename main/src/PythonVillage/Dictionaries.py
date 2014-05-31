from  main.src.InOut import *

fileName = 'rosalind_ini6'
fIn = open(getFullPathInput(fileName), 'r')
fOut = open(getFullPathOutput(fileName), 'w')
s = fIn.readline()
#s = 'We tried list and we tried dicts also we tried Zen'

dict = {}

for word in s.split():
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
for key, value in dict.items():
    fOut.write(key + ' ' + str(value) + '\n')
    print(key, value)

fIn.close()
fOut.close()