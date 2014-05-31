# Problem
#
# A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4) is a signed permutation of length 5.
#
# Given: A positive integer n≤6.
#
# Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
#
# Sample Dataset
#
# 2
# Sample Output
#
# 8
# -1 -2
# -1 2
# 1 -2
# 1 2
# -2 -1
# -2 1
# 2 -1
# 2 1
from main.src.InOut import *

fileName = 'output'
fOut = open(getFullPathOutput(fileName), 'w')

n = 5
lst = []
res = []
for c in range(1, n+1):
    res.append(c)
    lst.append(-c)
    lst.append(c)
used = []

count = 0
s = ''

def lex(pos):
    global count
    global s

    if pos == n:
        for x in res:
            s += str(x) + ' '
        s += '\n'
        count += 1
    else:
        for x in lst:
            if (abs(x) not in used):
                res[pos] = x
                used.append(abs(x))
                lex(pos+1)
                used.remove(abs(x))

lex(0)
fOut.write(str(count)+'\n')
fOut.write(s)

fOut.close()