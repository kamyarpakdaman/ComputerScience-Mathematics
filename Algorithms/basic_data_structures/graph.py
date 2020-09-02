# In this program, we will create a graph in python.

# The Vertex class keeps track of the value in a node and the edges/nodes
# connected to it;

class Vertex:
      
      def __init__(self, value):
            self.value = value
            self.edges = {}

      # This function adds an edge to a node and sets a value True for the
      # connection from a node to another one.

      def add_edge(self, vertex, weight = 0):
            self.edges[vertex] = weight

      # Getting a list of nodes connected to a node.

      def get_edges(self):
            return list(self.edges.keys())

# The Graph class will track all the vertices and handle higher level concerns 
# like whether the graph is directed or undirected.

class Graph:
      
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

    # Adding a new vertix to the graph.

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    # Adding a new edge between two nodes in the graph.

    def add_edge(self, from_vertex, to_vertex, weight = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
    
    # Checking if a path exists between two given nodes.

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]

        # We create the seen variable to ensure we don't get trapped in circles
        # in our while loop.

        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            if current_vertex == end_vertex:
                return True
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()

                # If the current_vertex isn't the end_vertex, we get the nodes connected to
                # the current_vertex and add them all to our start list, so that, we check them
                # for being the end_vertex. Further, in this step, we use our data in seen to
                # ensure we don't get to the same node again.

                next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
                start.extend(next_vertices)
        
        # If the while loop returns no True before the conclusion, it means no path is detected,
        # and hence, the function should return False.
        
        return False

print('\nThanks for reviewing')

# Thanks for reviewing
