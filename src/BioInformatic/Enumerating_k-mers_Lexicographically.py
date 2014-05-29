# Problem
#
# Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).
#
# Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.
#
# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
#
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.
#
# Sample Dataset
#
# T A G C
# 2
# Sample Output
#
# TT
# TA
# TG
# TC
# AT
# AA
# AG
# AC
# GT
# GA
# GG
# GC
# CT
# CA
# CG
# CC

dirName = 'InOut\\'
fileName = 'rosalind_lexf'
fIn = open(dirName + fileName + '.txt', 'r')
fOut = open(dirName + fileName + '_out.txt', 'w')

nt = fIn.readline().split()
n = int(fIn.readline())
# nt = 'T A G C'.split()
# n = 2
lst = ['' for c in range(0, n)]

def lex(pos):
    if pos == n:
        for x in lst:
            fOut.write(x)
        fOut.write('\n')
    else:
        for x in nt:
            lst[pos] = x
            lex(pos+1)

lex(0)

fIn.close()
fOut.close()