# CODE CHALLENGE: Solve the Overlap Graph Problem (restated below).
#      Input: A collection Patterns of k-mers.
#      Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.
#
# Sample Input:
#      ATGCG
#      GCATG
#      CATGC
#      AGGCA
#      GGCAT
#
# Sample Output:
#      AGGCA -> GGCAT
#      CATGC -> ATGCG
#      GCATG -> CATGC
#      GGCAT -> GCATG
from main.src.HelperFunctions.InOutHelper import *

fileName = 'rosalind_lexf'
fIn = open(getFullPathInput(fileName), 'r')
fOut = open(getFullPathOutput(fileName), 'w')

graph = {}
for line in fIn.readlines():
    line = line.strip()
    graph[line[:-1]] = line[1:]


fIn.close()
fOut.close()