# In this program, we use the famous Dijkstra's algorithm to find the shortest paths from a start vertex s
# to all vertices in a graph. We use the heapq data structure to efficiently take care of the vertices
# we explore.

from heapq import heappop, heappush
from math import inf

graph = {
  'A': [('B', 10), ('C', 3)],
  'C': [('D', 2)],
  'D': [('E', 10)],
  'E': [],
  'B': [('C', 3), ('D', 2)]
}

def dijkstras(graph, start):
      
      distances = {}

      # At first, we assume the distance from s to all vertices is infinity. Note that as we progress
      # in the algorithm, we replace the distances with the shortest distance found.

      for vertex in graph:
            
            distances[vertex] = inf
      
      # Setting the distance from s to itself as 0. Further, we start our exploration from start and
      # start checking its neighbors using a BFS-like algorithm.

      distances[start] = 0
      vertices_to_explore = [(0, start)]
      
      while vertices_to_explore:
            
            # At each loop, we draw the vertex from the heapq, which has the smallest distance, and explore
            # its neighbors.

            current_distance, current_vertex = heappop(vertices_to_explore)

            for neighbor, edge_weight in graph[current_vertex]:
                  
                  # Every time we get to a vertex, we re-compute the distance with our latest information.
                  # The latest information is actually the sum of the distance to the vertex at the tail of
                  # an edge and the weight of the edge to the vertext at the head of the edge. Then, if this
                  # new distance is smaller than the distance already assigned to the vertex at the head of
                  # the edge, we will replace the greater distance with the smaller one.

                  new_distance = current_distance + edge_weight

                  if new_distance < distances[neighbor]:
                        
                        distances[neighbor] = new_distance

                        # Then, we add the new distance for the vertex at the head of the edge to our heapq.
                        # Note that heapq takes care of sorting its data and keeps the shortest distance at
                        # the top of the list for later heappop().

                        heappush(vertices_to_explore, (new_distance, neighbor))
            
      return distances

print('\nThanks for reviewing')

# Thanks for reviewing
