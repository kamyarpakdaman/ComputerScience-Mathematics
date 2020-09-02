# In this program, we will define a class for nodes and then create a
# list of nodes with some specific capabilities.

# Defining a class for nodes.

class Node:

    # Taking a value for the node and an optional next node, which is
    # a Node class itself.

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    # A method for getting the value of a node.

    def get_value(self):
        return self.value
    
    # A method for getting the next node linked to a node.

    def get_next_node(self):
        return self.next_node
  
    # A method for setting the next node for a node.
    
    def set_next_node(self, next_node):
        self.next_node = next_node

# Definig a class for our linked list of node classes.

class LinkedList:

    # The LinkedList starts empty or with an object of Node class
    # as the head node of the list.

    def __init__(self, value=None):
        self.head_node = Node(value)
  
    # Getting the head node of a list.

    def get_head_node(self):
        return self.head_node
  
    # Inserting a new Node class object at the beginning of a list
    # and therefore, pushing the previous head node to being the
    # second node of the list.

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    # A method for printing out the values of the nodes in a list.

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
  
    # A method for removing the first node which has a specifi value.

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

print('\nThanks for reviewing')

# Thanks for reviewing   
