# In this program, we use a recursion implementation of Kosaraju's algorithm for finding the 
# top 5 largest strongly connected components (SCCs) of a graph. Although quite efficient for
# small graphs, this recursion implementation isn't efficient for massive graphs.

# Reading the graph from a text file and transofrming it into a dictionary:
# g = { v: [0, False, []]}
# In the list for each vertice, 0 is the t at first. The Boolean is used to track is a vertex is
# visited. Finally, the list at the end contains the edge head for which the tail is v.

# Note that, as of the algorithm, in the first round of DFS, we use the reverse graph, where 
# all edges are reversed.

file = open("sample_1.txt", "r") 
data = file.readlines()

g_rev = {}

for line in data:

    first_el = int(line.split()[0])
    second_el = int(line.split()[1])

    if first_el not in list(g_rev.keys()):

        g_rev[first_el] = [0, False, []]

    ex_rev = g_rev.get(second_el, None)

    if ex_rev is None:

        g_rev[second_el] = [0, False, [first_el]]

    else:

        g_rev[second_el][2].append(first_el)

# g_rev

# We use DFS, starting from the highest number labelled vertex. As we reach the end of paths,
# we assign the current t to the last vertex in the path, and then, we increment t.

t = 0

# Our goal in the first DFS is to find the times to reach for all vertices, which will be
# the new labels for the next round.

def DFS_first_loop(G):
    
    keys = list(G.keys())
    keys = sorted(keys, reverse = True)
    
    for i in keys:
                
        if not G[i][1]:
                        
            G = DFS_reverse(G, i)
        
        else: continue
    
    return G

# Running DFS with starting vertex i to get to the end of the path.

def DFS_reverse(G, i):
        
    global t
    
    G[i][1] = True
    
    for neighbor in G[i][2]:
                
        if not G[neighbor][1]:
            
            DFS_reverse(G, neighbor)
        
        else: continue
    
    # Incrementing t and adding it to the vertex value in the graph.
    
    t += 1
    G[i][0] = t
        
    return G

# In the new graph, t values for each vertex are modified, indicating when a vertex can
# be reached. Further, all the Booleans must be True.

new_g_rev = DFS_first_loop(g_rev)

# new_g_rev

# In this second round of DFS, we will use the new labels for each vertex and perform DFS
# on the original graph with the same edge relationships.

fhand = open('sample_1.txt')

new_g = {}

for line in fhand:
    
    first_el = int(line.split()[0])
    second_el = int(line.split()[1])
    
    new_first_el = new_g_rev[first_el][0]
    new_second_el = new_g_rev[second_el][0]
    
    if new_second_el not in list(new_g.keys()):
    
        new_g[new_second_el] = [0, False, []]
    
    ex_new = new_g.get(new_first_el, None)
    
    if ex_new is None:
        
        new_g[new_first_el] = [0, False, [new_second_el]]
        
    else:
        
        new_g[new_first_el][2].append(new_second_el)

# new_g

# The second loop DFS on the original graph with new vvertex labels.

def DFS_second_loop(G):
    
    leaders = []
    
    keys = list(G.keys())
    keys = sorted(keys, reverse = True)
    
    for i in keys:
        
        # print('In the outer loop, visited check, i: ', i)
        
        if not G[i][1]:
            
            # print('In the outer loop, not visited, i: ', i)
            
            s = i
            leaders.append(s)
            
            G = DFS(G, i, s)
    
    return G, leaders

# In this inner DFS, we don't track timing anymore, since we already have them. Instead, we track
# the leader vertices, which are the leaders representing SCCs. As we search the graph using DFS,
# As long as we can reach some vertices from a leader vertex, the leader vertex label will be added
# as value for each vertex in the dictionary, in the place where t used to be in the previous round.

def DFS(G, i, s):
    
    G[i][1] = True
    G[i][0] = s
    
    for neighbor in G[i][2]:
        
        if not G[neighbor][1]:
            
            DFS(G, neighbor, s)

    return G

# Here we have the new graph, where the first element indicates the leader for each vertex.

new_g_with_leaders, leaders = DFS_second_loop(new_g)

# new_g_with_leaders

# Finding the sizes for all existing SCCs using the leaders.

SCC_sizes = {}

for node in new_g_with_leaders:
    
    leader_finder = SCC_sizes.get(new_g_with_leaders[node][0], None)
    
    if leader_finder is None:
        
        SCC_sizes[new_g_with_leaders[node][0]] = 1
    
    else:
        
        SCC_sizes[new_g_with_leaders[node][0]] += 1

# SCC_sizes

# Finally, finding the top 5 largest SCCs.

SCC_sizes_rev = [(v, k) for (k, v) in SCC_sizes.items()]
top_5_SCC_sizes = sorted([v for (v, k) in SCC_sizes_rev], reverse = True)[:5]
top_5_SCC_sizes

print('\nThanks for reviewing')

# Thanks for reviewing
