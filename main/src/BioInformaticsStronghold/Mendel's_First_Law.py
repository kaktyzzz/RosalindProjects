# Problem
#
#
# Figure 2. The probability of any outcome (leaf) in a probability tree diagram is given by the product of probabilities from the start of the tree to the outcome. For example, the probability that X is blue and Y is blue is equal to (2/5)(1/4), or 1/10.
# Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.
#
# For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.
#
# Random variables can be combined to yield new random variables. Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.
#
# An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25 (see Figure 2 above).
#
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
#
# Sample Dataset
#
# 2 2 2
# Sample Output
#
# 0.78333

# population = [30, 23, 20]
# combination = [[1.0, 1.0, 1.0], [1.0, 0.75, 0.5], [1.0, 0.5, 0.0]]
# sumPop = 0
# for p in population:
#     sumPop += p
#
# class Tree:
#     def __init__(self, val, type, childrens):
#         self.val = val
#         self.type = type
#         self.childrens = childrens
#
#     def print(tree):
#         print(tree.val, tree.type)
#         for i in tree.childrens:
#             Tree.print(i)
#
#     def mult(tree):
#         global prob
#
#         for i in tree.childrens:
#             if tree.type != -1:
#                 t, t1 = tree.val
#                 t *= i.val[0]
#                 t1 *= i.val[1]
#                 i.val = (t, t1)
#                 prob += (t / t1) * combination[tree.type][i.type]
#             Tree.mult(i)
#
#
# probability = Tree((1, 1), -1, [])
#
# lastChildrens = []
# for r in range(0, 2):
#     if r == 0:
#         for pos, c in enumerate(population):
#             temp = Tree((c, sumPop), pos, [])
#             lastChildrens = probability.childrens
#             probability.childrens.append(temp)
#     else:
#         for child in lastChildrens:
#             ch, z = child.val
#             for pos, i in enumerate(population):
#                 c = ch
#                 if (child.type == pos):
#                     c -= 1
#                 temp = Tree((c, z-1), pos, [])
#                 child.childrens.append(temp)
#
# prob = 0;
# Tree.mult(probability)
# Tree.print(probability)
#
# print('%0.6f'%prob)

# Эта хрень не работает! =(

list = [29, 23, 18]
k, m, n = list
population = k + m + n
prob = (1.0 * k * (k-1)) / (population *(population-1))
prob += (1.0 * k * m) / (population *(population-1))
prob += (1.0 * k * n) / (population *(population-1))
prob += (1.0 * m * k) / (population *(population-1))
prob += (0.75 * m * (m-1)) / (population *(population-1))
prob += (0.5 * m * n) / (population *(population-1))
prob += (1.0 * n * k) / (population *(population-1))
prob += (0.5 * n * m) / (population *(population-1))
print('%.5f'%prob)