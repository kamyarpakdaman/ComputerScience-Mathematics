# In this program, we define a function which performs the BFS algorithms for searching graphs.

# In the Breadth-First Search algorithm, we steadily explore all the ways we can go and check them
# one by one.
   
def bfs(graph, start_vertex, target_value):
      
      path = [start_vertex]
      vertex_and_path = [start_vertex, path]
      bfs_queue = [vertex_and_path]
      
      visited = set()
      
      while bfs_queue:
            
            current_vertex, path = bfs_queue.pop(0)
            visited.add(current_vertex)

            for neighbor in graph[current_vertex]:
                  
                  if neighbor not in visited:
                        
                        if neighbor is target_value:
                              
                              return path + [neighbor]
                        
                        else:
                              
                              bfs_queue.append([neighbor, path + [neighbor]])

some_hazardous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
  }

print(bfs(some_hazardous_graph, 'sharks', 'bees'))

print('\nThanks for reviewing')

# Thanks for reviewing
