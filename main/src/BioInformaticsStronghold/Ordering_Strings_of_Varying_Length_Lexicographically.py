# Problem
#
# Say that we have strings s=s1s2⋯sm and t=t1t2⋯tn with m<n. Consider the substring t′=t[1:m]. We have two cases:
#
# If s=t′, then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).
# Otherwise, s≠t′. We define s<Lext if s<Lext′ and define s>Lext if s>Lext′ (e.g., APPLET<LexARTS because APPL<LexARTS).
# Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).
#
# Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
#
# Sample Dataset
#
# D N A
# 3
# Sample Output
#
# D
# DD
# DDD
# DDN
# DDA
# DN
# DND
# DNN
# DNA
# DA
# DAD
# DAN
# DAA
# N
# ND
# NDD
# NDN
# NDA
# NN
# NND
# NNN
# NNA
# NA
# NAD
# NAN
# NAA
# A
# AD
# ADD
# ADN
# ADA
# AN
# AND
# ANN
# ANA
# AA
# AAD
# AAN
# AAA

from main.src.HelperFunctions.InOutHelper import *

fileName = 'rosalind_lexv'
fIn = open(getFullPathInput(fileName), 'r')
fOut = open(getFullPathOutput(fileName), 'w')

nt = fIn.readline().split()
n = int(fIn.readline())
# nt = 'D N A'.split()
# n = 3
lst = []

def lex(pos):
    global lst
    if lst != []:
        for x in lst:
            fOut.write(x)
        fOut.write('\n')
    if pos < n:
        for x in nt:
            lst = lst[:pos]
            lst.append(x)
            lex(pos+1)
lex(0)

fIn.close()
fOut.close()