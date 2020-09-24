# In this program, we use Euclidan distane to implement the A* algorithm for finding the shortest
# path from a start vertex to a target vertex. Unlike the Dijkstra's algorithm, A* is optimized
# as a greedy algorithm fo follow the shortest path among some viabale options using the rough
# estimations from each vertex to the target vertex.

# At first, we create a class for our vertices. Note that x and y indicate the location longitude and
# latitude.

from math import inf, sqrt
from heapq import heappop, heappush

class graph_vertex:

    def __init__(self, name, x, y):

        self.name = name
        self.position = (x, y)

# Then, let's create a small sample graph with some vertices. We will not use these samples later. They
# are here just to know the structure of our graph.

thirty_third_and_madison = graph_vertex("33rd Street and Madison Avenue", 33, 4)
thirty_third_and_fifth = graph_vertex("33rd Street and 5th Avenue", 33, 5)

manhattan_graph = {
  thirty_third_and_madison: set([(thirty_third_and_madison, 1), (thirty_third_and_fifth, 3)]),
}

# Now, we define our heuristic functions, which uses locations' (x, y) for estimating the distance between 
# a given vertex and the target vertex.

def heuristic(start, target):
    
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])

    return sqrt(x_distance * x_distance + y_distance * y_distance)

# Below, we define the a_start algoithm, which uses the distance to a vertex, it's edge weight to a neighbor,
# and the neighbor's heuristic to the target vertex to decide which path to take.

def a_star(graph, start, target):
    
    paths_and_distances = {}

    for vertex in graph:

        paths_and_distances[vertex] = [inf, [start.name]]
    
    paths_and_distances[start][0] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore and paths_and_distances[target][0] == inf:

        current_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph[current_vertex]:

            new_distance = current_distance + edge_weight + heuristic(neighbor, target)
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
        
            if new_distance < paths_and_distances[neighbor][0]:
                
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path
                
                heappush(vertices_to_explore, (new_distance, neighbor))
    
    # It eventually returns the shortest path to the target vertex from the start vertex.

    return paths_and_distances[target][1]

print('\nThanks for reviewing')

# Thanks for reviewing
