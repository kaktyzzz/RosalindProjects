from __future__ import print_function
from src.HelperFunctions.InOutHelper import *

# fileName = 'input'
# fIn = open(getFullPathInput(fileName), 'r')
# text = fIn.readline().strip()

text1 = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
text2 = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'

c = 0
for i in range(0, len(text1)):
    if text1[i] != text2[i]:
        c += 1

print (c)

# fIn.close()