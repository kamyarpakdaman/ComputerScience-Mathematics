# In this program, we use a greedy algorithm for ordering weighted tasks in a way that we minimize the
# weighted sum of completion times. The raw data is a text file containing tasks data as follows:

# number_of_tasks
# task_1_weight task_1_length
# ...

# The algorithm will schedule the tasks in decreasing order of the ratio (weight/length)
# Side note: This algorithm is optimal and it does not matter how we break the ties.
# At the end we report the sum of weighted completion times of the resulting schedule.

import numpy as np
fhand = open('w1q1.txt')

# Here we build a dictionary which will contain the possible ratios for tasks as keys and the corresponding
# tasks as values in a list. E. g.:
# {0.16: [[8, 50], [4, 25], [4, 25], [8, 50]]}

dct = {}

for line in fhand:
    line = line.rstrip()
    items = line.split(' ')
    nitems = [int(x) for x in items]
    
    try:
        opt_object = nitems[0]/nitems[1]
        
        if dct.get(opt_object, 0) == 0:
            dct[opt_object] = [nitems]
            
        else:
            dct[opt_object].append(nitems)
    
    except: continue

# print(dct)

# As an unnecessary but cool step, we modify the dictionary and build nested dictionaries in which we gather
# tasks together based on their weights. I. e., after collecting tasks together based on their ratio, we collect
# the resulting tasks based on their weights. E. g.:
# {0.16: {8: [50, 50], 4: [25, 25]}}

for key in list(dct.keys()):
    ndct = {}
    
    for value in dct[key]:
        
        if ndct.get(value[0], 0) == 0:
            ndct[value[0]] = [value[1]]
            
        else:
            ndct[value[0]].append(value[1])
    
    dct[key] = ndct

# print(dct)

# Now we find the final ordering based on first, the ratio of tasks, and second, the weights of tasks per each
# category of ratio. Each element is a 2-item list containing respectively the weight and the length of the task.
# E. g.:
# [[99, 1],
# [98, 1]]

opt_objects = list(dct.keys())
opt_objects = sorted(opt_objects, reverse = True)

final_order = []

for key in opt_objects:
    ties = dct[key]
    weight_objects = list(ties.keys())
    weight_objects = sorted(weight_objects, reverse = True)
    
    for nested_key in weight_objects:
        
        for nested_value in ties[nested_key]:
            final_order.append([nested_key, nested_value])

# print(final_order)

# Next, in order to eventually compute the total weighted completion time, we need to compute the completion time
# individually for each task. E. g., if task 1 takes time 1 and task 2 takes time 3, task 2 is completed in 
# time (1+3) = 4

completion_times = []
initial_sum = 0

for item in final_order:
    initial_sum += item[1]
    completion_times.append(initial_sum)

# print(completion_times)

# Putting completiong times next to weights.

weights_completions = []

for i in range(len(final_order)):
    obj = [final_order[i][0], completion_times[i]]
    weights_completions.append(obj)

# print(weights_completions)

# Finally, computing individual weighted completion times and summing them up.

weighted_completion_times = [int(np.prod(item)) for item in weights_completions]
total_weighted_completion_times = sum(weighted_completion_times)
print(total_weighted_completion_times)

print('\nThanks for reviewing')

# Thanks for reviewing
