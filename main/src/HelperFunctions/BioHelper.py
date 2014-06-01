# Special Bioinformatics function
import os
from main.src.HelperFunctions.InOutHelper import *

import urllib.request

STOP_ANTICODON = 'Stop'
URL_UNIPROT = 'http://www.uniprot.org/uniprot/'

def getRNACodonTable():
    f = open(getFullPathOther('rna_codon_table.txt'), 'r')
    resDict = {}
    for line in f:
        key, value = line.split()
        resDict[key] = value
    return  resDict

def readFASTA(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line[1:], []       #Убирает знак ">" из имени
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

def getUniProtFASTA(ProtID):
    res = urllib.request.urlopen(URL_UNIPROT + ProtID + '.fasta').read().decode('utf-8')
    return res
