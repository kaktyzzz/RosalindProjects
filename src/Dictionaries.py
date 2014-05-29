fileName = 'rosalind_ini6'
fIn = open(fileName + '.txt', 'r')
s = fIn.readline()
#s = 'We tried list and we tried dicts also we tried Zen'
fOut = open(fileName + '_out.txt', 'w')
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