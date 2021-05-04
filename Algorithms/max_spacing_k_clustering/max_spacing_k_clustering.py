# In this program, we build a clustering algorithm for computing a max-spacing k-clustering. The data describes
# a complete graph with edge costs in the below format:

# number_of_nodes
# edge_1_node_1 edge_1_node_2 edge_1_cost
# ...

# Note that there is at most one edge per a given pair of nodes.

# We build analgorithm to cluster these vertices in 4 clusters, and then we find out the maximum spacing of this
# clustering, that is, the minimum distance between a given pair of clusters. This is a greedy algorithm which, at each step,
# detects a pair of nodes that are closest to each other than any other pair of nodes, and clusters them together. If either or
# both of them are already in clusters, the algorithm combines all nodes in one cluster. The process goes on until we reach the
# desired number of clusters, k.

import heapq
import math

# reading data from the file.

fhand = open('raw.txt')

# Here we make a distionary mapping from node 1 to a list of nested lists each of which containing the other
# node of an edge originating from node 1 and its cost in the format below:

# {1: [[2, 6808], ...], ...}

dct = {}
for x in range(1, 501):
    dct[x] = []

for line in fhand:
    line = line.rstrip()
    items = line.split(' ')
    if len(items) == 1: continue
    
    dct[int(items[0])].append([int(items[1]), int(items[2])])
    
    dct[int(items[1])].append([int(items[0]), int(items[2])])

#print(dct)

# Reading the file again to generate a list of all edges including their nodes and costs in the below format:

# [[1, 2, 6808], ...]

fhand = open('raw.txt')

lst = []

for line in fhand:
    line = line.rstrip()
    items = line.split(' ')
    items = [int(x) for x in items]
    
    if len(items) == 1: continue
    
    lst.append([items[0], items[1], items[2]])

#print(lst)

# Here we build a heapq instance which will later help us in extracting the minimum cost edge at each step.

h = []
for item in lst:
    heapq.heappush(h, (item[2], [item[0], item[1]]))

#print(h)

# Now we build and run a clustering algorithm. The list init_lst contains the clusters. at the beginning, we assume
# each node is its own cluster.

init_lst = list(range(1, 501))

while len(init_lst) > 4:
    closest_pair = heapq.heappop(h) # Extracting the closest pair of nodes from our heap. Ties are broken based on heap.
    node_1 = closest_pair[1][0]
    node_2 = closest_pair[1][1]
    
    # Using flags, we detect if the two sides of the current closest pair are included in some cluster already.
    
    flag_1 = 0
    flag_2 = 0
    
    if node_1 in init_lst:
        flag_1 = 1
    
    if node_2 in init_lst:
        flag_2 = 1
        
    # Condition one. Both nodesare in main init_lst and not combined as of being in the same cluster.
    # We simply remove them from the main list and put them together in a nested list.
    
    if (flag_1 == 1) and (flag_2 == 1):
        init_lst.remove(node_1)
        init_lst.remove(node_2)
        init_lst.append([node_1, node_2])
    
    # Condition two. One node is not added to a cluster, while the other is.
    # We remove the node which isn't added to a cluster from the main list and add it to the appropriate
    # cluster based on the other node, which is already in a nested list indicating a cluster.
    
    if (flag_1 == 1) and (flag_2 == 0):
        
        for i in init_lst:
            
            try:
                
                if node_2 in i:
                    existing_cluster = i
            
            except: pass
        init_lst.remove(existing_cluster)
        init_lst.remove(node_1)
        existing_cluster.append(node_1)
        new_cluster = existing_cluster
        init_lst.append(new_cluster)
    
    if (flag_1 == 0) and (flag_2 == 1):
        
        for i in init_lst:
            
            try:
                
                if node_1 in i:
                    existing_cluster = i
                    break
            
            except: pass
        init_lst.remove(existing_cluster)
        init_lst.remove(node_2)
        existing_cluster.append(node_2)
        new_cluster = existing_cluster
        init_lst.append(new_cluster)
    
    # condition three. Both nodes are already in a nested list.
    # In this case we in fact have two clusters that two of their members are so close that we can combine them
    # as one cluster, and we do so by removing both clusters and adding a combined nested list to the main list.
    
    if (flag_1 == 0) and (flag_2 == 0):
        
        for i in init_lst:
            
            try:
                
                if node_1 in i:
                    first_cluster = i
            
            except: pass
        
        for i in init_lst:
            
            try:
                
                if node_2 in i:
                    second_cluster = i
            
            except: pass
        
        if first_cluster != second_cluster:
            init_lst.remove(first_cluster)
            init_lst.remove(second_cluster)
            new_cluster = first_cluster
            
            for item in second_cluster:
                new_cluster.append(item)
            
            init_lst.append(new_cluster)
        
        else: pass

# By the end of the while loop, we reach to a 4-clustering.

#print(init_lst)

# Finally, to compute the maximum-spacing, or equivalently the minimum distance between any pair of clusters,
# we just compare the distances by using clusters and the list we had earlier which contained edges and their costs.

min_distance = math.inf

for i in range(len(init_lst)-1):
    for j in range(len(init_lst)-1):
        if init_lst[i] != init_lst[j]:
            nodes_edges = dct.get(init_lst[i])
            for item in nodes_edges:
                if item[0] == init_lst[j]:
                    val = item[1]
                    if val < min_distance:
                        min_distance = val

for i in range(len(init_lst)-1):
    for j in init_lst[3]:
        if init_lst[i] != j:
            nodes_edges = dct.get(init_lst[i])
            for item in nodes_edges:
                if item[0] == j:
                    val = item[1]
                    if val < min_distance:
                        min_distance = val

print(min_distance)

print('\nThanks for reviewing')

# Thanks for reviewing
