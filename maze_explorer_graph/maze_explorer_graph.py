# In this program, we will use a graph to map a twisted maze. We will act as a maze runner and 
# explore the graph until we reach the treasure room.

# At first, we define classes for vertices and graphs. More explanation on how 
# these classes and methods work can be found here:
# https://github.com/kamyarpakdaman/ComputerScience-Mathematics/blob/master/Algorithms/basic_data_structures/graph.py

# We use the vertex class to create our graph vertices.

class Vertex:
    
    def __init__(self, value):
        
        self.value = value
        self.edges = {}

    def add_edge(self, adjacent_value, weight = 0):
        
        self.edges[adjacent_value] = weight

    def get_edges(self):
        
        return self.edges.keys()

# We use the Graph class to create our complete graph.

class Graph:
    
    def __init__(self):

        self.graph_dict = {}

    def add_vertex(self, node):
        
        # Note that in the dictionary, the value is the key, and the vertex class is the value. 
        
        self.graph_dict[node.value] = node

    def add_edge(self, from_node, to_node, weight = 0):

        self.graph_dict[from_node.value].add_edge(to_node.value, weight)
        self.graph_dict[to_node.value].add_edge(from_node.value, weight)

    # We know that we want to find the treasure room starting our discovery from the entrance room.

    def explore(self):

        print("Exploring the graph....\n")

        current_room = 'entrance'
        path_total = 0

        print("\nStarting off at the {}\n".format(current_room))

        while current_room != 'treasure_room':

            node = self.graph_dict[current_room]

            for connected_room, weight in node.edges.items():

                key = connected_room[0]

                # Guiding the user through the maze at each room. We actually let him/her know where
                # (s)he can head from his/her current room forward.

                print("enter {} for {}: {} cost".format(key, connected_room, weight))

            valid_choices = [key[0] for key in node.edges.keys()]

            print("\nYou have accumulated: {} cost".format(path_total))

            choice = input("\nWhich room do you move to? ")

            if choice not in valid_choices:

                print("please select from these letters: {}".format(valid_choices))
            
            else:

                for room in node.edges.keys():

                    if room.startswith(choice):
                        
                        # Taking the user to the new room (s)he has chosen to move to.

                        current_room = room
                        path_total += node.edges[room]
                
                print("\n*** You have chosen: {} ***\n".format(current_room))
        
        print("Made it to the treasure room with {} cost".format(path_total))

    
    def print_map(self):

        print("\nMAZE LAYOUT\n")

        for node_key in self.graph_dict:

            print("{0} connected to...".format(node_key))
            node = self.graph_dict[node_key]

            for adjacent_node, weight in node.edges.items():
                
                print("=> {0}: cost is {1}".format(adjacent_node, weight))
            
            print("")
        
        print("")

# In this function, we create our graph using the classes we have already created.

def build_graph():
    
    graph = Graph()

    # Making some rooms.
    
    entrance = Vertex('entrance')
    ante_chamber = Vertex('ante_chamber')
    kings_room = Vertex('king\'s room')
    grand_gallery = Vertex('grand gallery')
    treasure_room = Vertex('treasure room')

    graph.add_vertex(entrance)
    graph.add_vertex(ante_chamber)
    graph.add_vertex(kings_room)
    graph.add_vertex(grand_gallery)
    graph.add_vertex(treasure_room)

    # Connecting the rooms.

    graph.add_edge(entrance, ante_chamber, 7)
    graph.add_edge(entrance, kings_room, 3)
    graph.add_edge(kings_room, ante_chamber, 1)
    graph.add_edge(grand_gallery, ante_chamber, 2)
    graph.add_edge(grand_gallery, kings_room, 2)
    graph.add_edge(treasure_room, ante_chamber, 6)
    graph.add_edge(treasure_room, grand_gallery, 4)

    # Reviewing the graph.

    graph.print_map()

    return graph

# Below, we use our graph and start exploring the rooms.

excavation_site = build_graph()
excavation_site.explore()

print('\nThanks for reviewing')

# Thanks for reviewing
