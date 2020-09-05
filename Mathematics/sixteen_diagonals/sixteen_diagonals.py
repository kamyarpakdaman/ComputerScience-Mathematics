# The problem is we want to know if it is possible to put 16 diagonals in 
# the squares of a 5 x 5 grid, such that no two diagonals touch each other.
# We'll use backtracking to solve this problem. Note that some squares will
# be left empty.

# This function takes a permutation as an argument and investigates whether
# or not its last square diagonal status conflicts with the previous ones. Note that
# firstly, having a BL to TR diagonal corresponds to value +1, having a TL to
# BR diagonal corresponds to value -1, and having no diagonal corresponds to
# value 0. Secondly, this function turns the square grids into a list and 
# retrieves the last square as perm[-1]. Other squares which might be affected by
# this last square, are named as point_1 to point_4. As of the last square diagonal
# status (+1, -1 and 0), the function determines whether the last square diagonal
# status conflicts with the previous saquares or not. Note that the function, 
# eventually returns True/False.

def can_be_extended(perm):

    length = len(perm)
    rem = length%5

    if length == 1:
        return True
    
    if length > 1 and length <= 5:
        point = perm[-1]
        point_1 = perm[-2]

        if point == 0:
            return True
        elif point == +1:
            if point_1 == -1:
                return False
            else:
                return True
        elif point == -1:
            if point_1 == +1:
                return False
            else:
                return True
    else:
        if rem == 1:
            point = perm[-1]
            point_2 = perm[-5]
            point_3 = perm[-6]

            if point == 0:
                return True
            elif point == +1:
                if point_2 == +1 or point_3 == -1:
                    return False
                else:
                    return True
            elif point == -1:
                if point_3 == +1:
                    return False
                else:
                    return True

        elif rem >= 2 and rem <= 4:
            point = perm[-1]
            point_1 = perm[-2]
            point_2 = perm[-5]
            point_3 = perm[-6]
            point_4 = perm[-7]

            if point == 0:
                return True
            elif point == +1:
                if point_1 == -1 or point_2 == +1 or point_3 == -1:
                    return False
                else:
                    return True
            elif point == -1:
                if point_1 == +1 or point_3 == +1 or point_4 == -1:
                    return False
                else:
                    return True

        elif rem == 0:
            point = perm[-1]
            point_1 = perm[-2]
            point_3 = perm[-6]
            point_4 = perm[-7]

            if point == 0:
                return True
            elif point == +1:
                if point_1 == -1 or point_3 == -1:
                    return False
                else:
                    return True
            elif point == -1:
                if point_1 == +1 or point_3 == +1 or point_4 == -1:
                    return False
                else:
                    return True

# This function starts with an empty list as prem = [] and takes the number of squares
# possible, and one by one, assigns a diagonal status to each square (+1, -1, or 0). The
# function then uses the can_be_extended fuction to determines whether a newly added diagonal
# to a square conflicts with the previous ones or not. Here we get rid of the dead ends in
# the recursion tree. The functions goes ahead until under the limitation of max length for
# the premutation list until it finally catches the premutation with no conflict consisting
# 16 diagonals in a 5 x 5 grid. 

def extend(perm, n):

    # Since we know the answer is yes, to help the cpu, we add this part so that it directly
    # looks for the outcomes containing 16 diagonals and omitting the outcomes with, say, 15
    # diagonals or less. 

    count = 0
    for i in perm:
        if i != 0:
            count += 1
    
    if len(perm) == n and count == 16:
        print(perm)
        exit()

    for j in [1, 0, -1]:

        # Maintaining the length limitation.
        if len(perm) < n:
            
            # Adding the diagonal status values one by one to each square.
            perm.append(j)
            # print('perm is ', perm, 'with len ', len(perm), '\n')
            if can_be_extended(perm):
                # print("True retrieved\n")
                # If the way we're going isn't a dead end yet, we go deeper into the recursion tree.
                extend(perm, n)
            # print('False retrieved\n')
            # If there's a dead end with a newly added diagonal status, we omit it and replace it
            # with our next option.
            perm.pop()
            # print('perm after pop is ', perm, 'with len ', len(perm), '\n')

extend(perm = [], n = 25)

print('\nThanks for reviewing')

# Thanks for reviewing
