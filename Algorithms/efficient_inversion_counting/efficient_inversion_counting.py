# In this program, we will count the inversions on an array using a Divide and Conquer algorithm.

# This function is given two arrays and the inversions already counted when creating each of them.
# It then returns the inversions between them, through performing a merge sorting process.

def split_inversion_counter(left, left_inv, right, right_inv):
    
    sorted_list = []
    inner_inversions = left_inv + right_inv
    
    left = list(left)
    right = list(right)
    
    while (left and right):
        
        if left[0] < right[0]:
            
            sorted_list.append(left[0])
            left.pop(0)
        
        # Handling equal elements in the two lists. They are not counted a inversions.

        elif left[0] == right[0]:
            
            sorted_list.append(left[0])
            sorted_list.append(right[0])
            left.pop(0)
            right.pop(0)
            
        else:
            
            sorted_list.append(right[0])
            inner_inversions += len(left)
            right.pop(0)
    
    if left:

        sorted_list += left
    
    if right:
        
        sorted_list += right

    return sorted_list, inner_inversions
        
# This function is given an array and through breaking it into halves, recursively finds out the
# number of inversions in the array and its sub-arrays.

def inv_counter(array):
    
    # The base case; where a single element array is returned with 0 inversions.

    n = len(array)
    if n <= 1:
        return array, 0
    
    left = array[:(n//2)]
    right = array[(n//2):]

    left_sorted, left_inversions = inv_counter(left)
    right_sorted, right_inversions = inv_counter(right)
 
    
    sorted_lst, inversions_count = split_inversion_counter(left_sorted, left_inversions, right_sorted, right_inversions)
          
    return sorted_lst, inversions_count

# As an example, we will read an array from a text file; and then, we'll count the number of inversions.

import numpy as np

file = open('data.txt')
lst = []
    
for item in file:
    item = item.rstrip()
    lst.append(int(item))

arr = np.array(lst) 

sorted_list, number_of_inversions = inv_counter(arr)
# print(number_of_inversions)

print('\nThanks for reviewing')

# Thanks for reviewing
