# Special Bioinformatics function
import os
from main.src.HelperFunctions.InOutHelper import *

import urllib.request

STOP_ANTICODON = 'Stop'
URL_UNIPROT = 'http://www.uniprot.org/uniprot/'

def comp(dna):
    ntType = ['A', 'C', 'G', 'T']
    complDict = dict(zip(ntType, ntType[::-1]))
    result = ''.join(complDict[nt] for nt in dna[::-1])
    return result

def RNAtoDNA(rna):
    ntDict = {ord('U'):'T'}
    dna = rna.translate(ntDict)
    return dna

def DNAtoRNA(dna):
    ntDict = {ord('T'):'U'}
    rna = dna.translate(ntDict)
    return rna

def getRNACodonTable():
    f = open(getFullPathOther('rna_codon_table.txt'), 'r')
    resDict = {}
    for line in f:
        key, value = line.split()
        resDict[key] = value
    return  resDict

def getMassTable():
    f = open(getFullPathOther('mass.txt'), 'r')
    resDict = {}
    for line in f:
        key, value = line.split()
        resDict[key] = int(value)
    return  resDict

def getMassPeptides(pep):
    massTable = getMassTable()
    mass = 0
    for p in pep:
        if massTable.get(p) != None:
            if p == '':
                mass += 0
            else:
                mass += massTable[p]
    return mass

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
