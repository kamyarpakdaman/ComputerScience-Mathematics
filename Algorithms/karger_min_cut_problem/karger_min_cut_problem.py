#!/usr/bin/env python
# coding: utf-8

# In[229]:


import numpy as np
import re


# In[232]:


def potential_min_cut_finder(g):
    
    from random import randint, choice
    
    vertices = list(g.keys())    
    n_vertices = len(g.keys())
    
    if n_vertices == 2:

        return len(g[list(g.keys())[0]])
    
    random_vertice = choice(vertices)
    random_edge_other_vertice = choice(g[random_vertice])
    
    for vertice in g[random_edge_other_vertice]:
        
        if vertice != random_vertice:
            
            g[random_vertice].append(vertice)
            
        g[vertice].remove(random_edge_other_vertice)
                
        if vertice != random_vertice:
            
            g[vertice].append(random_vertice)
    
    del g[random_edge_other_vertice]
    
    return potential_min_cut_finder(g)


# In[ ]:


min_cut = None

for i in range(50):
    
    data = open('data.txt')
    
    g = {}

    for line in data:

        line_data = re.findall('\d+', line)
        g[int(line_data[0])] = []

        for v in line_data[1:]:

            g[int(line_data[0])].append(int(v))
    
    last_count = potential_min_cut_finder(g)
    
    if not min_cut or last_count < min_cut:
        
        min_cut = last_count
    
print(min_cut)

print('\nThanks for reviewing')

# Thanks for reviewing
