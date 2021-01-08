# In this program we implement the Median Maintenance algorithm. In this algorithm, we use MinHeap and 
# MaxHeap data structures for step-by-step calculation of the median of a sequence of numbers when the
# numbers are fed as a stream. This is a fast solution with O(log i), where i is the number of numbers
# in the stream. Note that this program doesn't apply for streams containing repetitions.

# At each step, we keep the half smaller values in the low heap which is a MaxHeap, and the larger half
# in the high heap which is a MinHeap. Consequently, after adding each new number, our new median would
# be either the new entry, the maximum of the lower heap, or the minimum of the higher heap.

import heapq

m_values = []
low_cat = []
high_cat = []

# The text file contains a list of the integers from 1 to 10000 in unsorted order.

fh = open('data.txt')
lst = []
for line in fh:
        lst.append(int(line.split()[0]))

# heapq library only provides us with a MinHeap. Instead of creating a MaxHeap data structure, we use a
# trick and add integers multiplied by -1 to this heap. As a result, the MaxHeap min value at each step
# would actually be its maximum.

# Here we initiate our heaps using two values. Note that since the MaxHeap contains the smaller half, we
# initiate it with 0 so that every entry is smaller than it (because entries are multiplied by -1). Based
# on the same logic, we initiate the MinHeap with 10001 so that every entry is smaller than it. I. e., we
# actually initiate the heaps with two numbers that we will never extract from the heap.

heapq.heappush(low_cat, 0)
heapq.heappush(high_cat, 10001)

# By reading each new entry from the stream, we might face different conditions based on two main factors:
# (1) the lengths of the halves, and (2) comparison of the new entry with current min and max values. 

# And this is the criterion for determining the median at each step after adding the new entry:
# Let's say total read numbers (including both low and high heaps) contains k elements. If k is odd, median
# would be the ((k+1)/2)th smallest number. If k is even, median would be the (k/2)th smallest number.

for i in range(len(lst)):
    
    new = lst[i]
    
    max_low = -1*low_cat[0]
    len_low = len(low_cat)
    min_high = high_cat[0]
    len_high = len(high_cat)
    
    if len_low == len_high:
        
        if new < max_low:
            median = max_low
            m_values.append(median)
            heapq.heappush(low_cat, -1*new)
        
        elif new > min_high:
            median = min_high
            m_values.append(median)
            heapq.heappush(high_cat, new)
        
        elif new > max_low and new < min_high:
            median = new
            m_values.append(median)
            heapq.heappush(low_cat, -1*new)
    
    elif len_low == len_high + 1:
                
        if new < max_low:
            heapq.heappop(low_cat)
            heapq.heappush(high_cat, max_low)
            heapq.heappush(low_cat, -1*new)
            median = -1*low_cat[0]
            m_values.append(median)
        
        elif new > min_high:
            median = max_low
            m_values.append(median)
            heapq.heappush(high_cat, new)
        
        elif new > max_low and new < min_high:
            median = max_low
            m_values.append(median)
            heapq.heappush(high_cat, new)
    
    elif len_high == len_low + 1:
                
        if new < max_low:
            median = max_low
            m_values.append(median)
            heapq.heappush(low_cat, -1*new)
        
        elif new > min_high:
            heapq.heappop(high_cat)
            heapq.heappush(low_cat, -1*min_high)
            heapq.heappush(high_cat, new)
            median = -1*low_cat[0]
            m_values.append(median)
        
        elif new > max_low and new < min_high:
            median = new
            m_values.append(median)
            heapq.heappush(low_cat, -1*new)
    else:
        print('Weird case visited')
        break

print('\nThanks for reviewing')

# Thanks for reviewing
