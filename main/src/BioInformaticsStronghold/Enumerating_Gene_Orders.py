# Problem
#
# A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.
#
# Given: A positive integer n≤7.
#
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
#
# Sample Dataset
#
# 3
# Sample Output
#
# 6
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

from main.src.InOut import *

fileName = 'output'
fOut = open(getFullPathInput(fileName), 'w')

n = 7
lst = [c for c in range(1, n+1)]
used = []

fact = 1
for c in lst:
    fact *= c
fOut.write(str(fact)+'\n')
def lex(pos):
    if pos == n:
        for x in lst:
            fOut.write(str(x) + ' ')
        fOut.write('\n')
    else:
        for x in range(1, n+1):
            if (x not in used):
                lst[pos] = x
                used.append(x)
                lex(pos+1)
                used.remove(x)

lex(0)
fOut.close()
