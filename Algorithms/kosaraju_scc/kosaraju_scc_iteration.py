# In this program, we use an iterative implementation of Kosaraju's algorithm for finding the 
# top 5 largest strongly connected components (SCCs) of a graph. This algorithm is quite
# efficient for massive graphs.

# Reading the graph from a text file and transofrming it into adjacency lists where the index
# indicates the vertice label and the value indicates the edges:
# g = [[1], [3, 5], [2, 6], ...]

# Further, we track visiting the vertices using a visited list; and we use scc list to denote
# the leader for each vertiex in the final round.

# Note that, as of the algorithm, in the first round of DFS, we use the reverse graph, where 
# all edges are reversed.

import pandas as pd

num_nodes, file_name = 9, 'sample_1.txt'

gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

visited = [False] * num_nodes

scc = [0] * num_nodes

stack = [] 
order = [] 


file = open(file_name, "r") 
data = file.readlines()

for line in data:
    items = line.split()
    gr[int(items[0]) - 1] += [int(items[1]) - 1]
    r_gr[int(items[1]) - 1] += [int(items[0]) - 1]

# This is the first stack implementation of our DFS. Starting from the vertex with the 
# largest label, we add vertices to the top of the label until we reach a dead-end. When it is
# the case, the last vertex visited will be added to the orders list. Then we go back and add
# vertices to the orders list until we reach a vertex which has an outgoing, unvisited edge. We
# will take the path to the end and follow this process until all vertices are visited. The order
# list at the end, will denote the reversed order through which we should perform the second DFS.

for node in range(num_nodes-1, -1, -1):
        
    if (not visited[node]):
        
        stack.append(node)
        visited[node]=True
        
        while stack:
            
            stack_node = stack[-1]
            
            for head in r_gr[stack_node]:
                
                if (not visited[head]):
                    
                    stack.append(head)
                    visited[head]=True
                    
                    stack_node = stack[-1]
                    
                else: continue
            
            count = 0
            
            for item in r_gr[stack_node]:
                
                if visited[item] is False:
                    
                    count += 1
                    
            if (len(r_gr[stack_node]) < 1) or (count == 0):
                
                order.append(stack_node)
                stack.pop(len(stack) - 1)

# Alright! We have the reversed order, which we reverse below to have the order we want. Further,
# since we are running DFS again, we let all vertices be unvisited again.

visited = [False] * len(visited) 
order.reverse()

s = None

# In this second round of DFS, we denote the first vertex of a path as the leader path, and add it
# as the leader for all vertices in that path in the scc list.

for node in order:
    
    if (not visited[node]):
        
        stack.append(node)
        visited[node]=True
        
        s = node
        
        while stack:
            
            stack_node = stack[-1]
            scc[stack_node] = s
            
            for head in gr[stack_node]:
                
                if (not visited[head]):
                    
                    stack.append(head)
                    visited[head]=True
                    
                    stack_node = stack[-1]
                    scc[stack_node] = s
            
            count = 0
            
            for item in gr[stack_node]:
                
                if visited[item] is False:
                    count += 1
                    
            if (len(gr[stack_node]) < 1) or (count == 0):
                
                order.append(stack_node)
                stack.pop(len(stack) - 1)


# Finding the sizes for all existing SCCs using the leaders.

scc.sort(reverse=True)
series = pd.Index(scc)
sizes = series.value_counts().reset_index()
result = sorted(list(sizes[0]), reverse = True)

# Finally, finding the top 5 largest SCCs.

result[:5]

print('\nThanks for reviewing')

# Thanks for reviewing
