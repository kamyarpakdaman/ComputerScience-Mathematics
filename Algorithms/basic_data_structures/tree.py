# In this program, we're creating a very simple tree with some capabilities.

class TreeNode:

    def __init__(self, value):

        self.value = value
        self.children = []

    def add_child(self, child_node):

        print("Adding " + child_node.value)
        self.children.append(child_node) 
    
    def remove_child(self, child_node):

        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children if child is not child_node]

    # Extracting all children in a tree.

    def traverse(self):

        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

print('\nThanks for reviewing')

# Thanks for reviewing 
