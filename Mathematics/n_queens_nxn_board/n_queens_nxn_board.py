# We want to know if it is possible to put N queens in an n x n chessboard
# such that no two queens attack each other. We already know that essentially
# each column/row will contain one and only one queen, not more, not less. 
# This idea leads us through using permutations as arrays. Let's say
# perm = [1, 3, 0, 2]. Considering the indices as 0, 1, 2 and 3, and imagining
# a 4 x 4 chessboard, we can see that in column with indice of 0, the queen is
# placed in row 1 and so on. The general idea is to find one permunation in
# which both there's one and only one queen per column/row, and that no two
# queens are on the same diagonal. Let's do it.

# At first, we use itertools library to create a general solution.

from itertools import permutations
from itertools import combinations

# Cells [i1, j1] and [i2, j2] are on the same diagonal if and only if
# abs(i1-i2) == abs(j1-j2)

def is_solution(perm):
    for (i1, i2) in combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]): return False
    return True

# Here we generate all possible permutations and check all with is_solution
# function. As soon as one valid permutation is found, we're done.

n = int(input('Enter n: \n'))

# Note that this way of solving, although seeming good, is too slow for large
# amounts of n. Therefore, we just get the n here as input and actually jump
# over the poor solution to the optimized solution later on.
if 'black' == 'white':
    for perm in permutations(range(n)):
        if is_solution(perm):
            print(perm)
            exit()

# This function generates all possible permutations for an n x n chess board
# in which each column/row has one and only one queen positioned in it. Note 
# that this is a recursive function.

def generate_permutations(perm, n):
    if len(perm) == n:
        print(perm)
        return
    for k in range(n):
        if k not in perm:
            perm.append(k)
            generate_permutations(perm, n)
            # We pop the last added k to start creating new permutations.
            perm.pop()

# As mentioned earlier, we need a faster, more optimized solution. We'll use Backtracking,
# which, in our context, means that for each partially formed permutation, we check if
# by extending it we can generate a valid output or not. If this is not the case, we'll
# just go no more into it and let it go. This is why this way of solving is way faster.
# We actually omit the dead ends in the big recursion tree and find where we have a chance
# for winning.

# In this function, for any given perm, we check if the perm immediately after omitting
# the last item is valid or not. I. e., we omit the last element from the given perm and
# check the new smaller perm to be valid. 

def can_be_extended(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]): return False
    return True

# Combining the previous functions and making a fast, optimized solution.

def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()
    for k in range(n):
        if k not in perm:
            perm.append(k)
            if can_be_extended(perm): extend(perm, n)
            perm.pop()

# Performing the solution for the given n and finding the solution permunation
# or getting nothing back if it's just not possible to place N queens in an nxn
# chess board. Note that we put the initial value for perm as [] to have all
# possible permunations available.

extend(perm = [], n = n)

print('\nThanks for reviewing')

# Thanks for reviewing
