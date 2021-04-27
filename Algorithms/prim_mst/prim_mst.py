# In this program, we use Prim's algorithm, which is a greedy one, for finding the MST of a given graph. The raw data is a text file 
# containing a graph as follows:

# number_of_vertices number_of_edges
# one_node_of_edge_1 another_node_of_edge_1 edge_1_cost
# ...

# This algorithm finds the Minimum Spanning Tree of the graph using Prim's algorithm and eventually we report
# the overall cost of the MST. 

# While the straightforward implementation has a running time of O(mn), by using heap data structure, the
# performance is enhanced.

import heapq
fhand = open('raw.txt')

# Here we move the data from text file to a dictionary and form our graph. Each key is an origin node and the value
# contains destination nodes and corresponding edge costs. E. g.:

# {1: [[2, 6807],
#  [132, -151]]}

dct = {}
for x in range(1, 501):
    dct[x] = []

for line in fhand:
    line = line.rstrip()
    items = line.split(' ')
    if len(items) == 2: continue
    
    dct[int(items[0])].append([int(items[1]), int(items[2])])
    
    dct[int(items[1])].append([int(items[0]), int(items[2])])

# print(dct)

# Now we develop the algorithm. It starts with an arbitrary vertice and repeatedly checks all edges between a
# already_visited_set of vertices and the rest of them to find the cheapest edge. Then then edge is added to the
# MST and the destination node is added to the already_visited_set.

V = list(dct.keys())

X = [1] # The list of vertices already visited.
T = [] # The list of edges included in the MST.
V_X = [item for item in V if item not in X] # The rest of edges, or those not visited yet.

while X != V: # Note that an MST contains all vertices of a graph. Hence, we repeat the loop until all nodes are in.
    h = [] # The heap.

    # We iterate and find all existing edges between X and V_X and add their edges to the heap.

    for first_v in X:
        for second_v in V_X:
            for v_e in dct[first_v]:
                if v_e[0] == second_v:
                    heapq.heappush(h, (v_e[1], [first_v, v_e[0]]))
    #print("Heap is ", h)
    
    # Here we extract the edge with the minimum cost. Then we omit its destination node from V_X and add it to X.
    try:
        min_edge_node = heapq.heappop(h)
        #print("Min edge is ", min_edge_node, "\n")
        X.append(min_edge_node[1][1])
        T.append(min_edge_node)
        V_X = [item for item in V if item not in X]
    
    except: break

# print(T)

# Extracting costs from T. Note that we have added costs and origin-destination nodes of edges to T already.

costs = [int(x[0]) for x in T]
# print(costs)

# Finally, reporting the overal cost of the MST.

overal_cost = sum(costs)
print(overal_cost)

print('\nThanks for reviewing')

# Thanks for reviewing
