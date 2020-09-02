# In this program, we will define a class for nodes and then create a
# class for stacks with some capabilities. Then we will order some pizzas.

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

# Defining a class for stacks.

class Stack:
    
    # The stack will have a size limit of 1000 as default, and the size
    # of the stack will be zero at the beginning.
    
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit
    
    # To push a value at top of the stack, after we make sure there is
    # enough size, we will first create a new node with the given value,
    # then add the current top value as the link for the new top value,
    # and finally replacing the old top value with the new one.
    
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the pizza stack!".format(value))
        else:
            print("No room for {}!".format(value))
    
    # To pop the stack, after making sure there is at least one node in it,
    # we will first save the current top item in a variable to avoid its
    # loss; then, we will set the linked value to the current top item as
    # the new top item, and finally, we will return the old top item's value.
    # Further, the size will decrease for one point.
    
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value())
            return item_to_remove.get_value()
        print("All out of pizza.")
    
    # To peek the stack, we will simply return the value of the top node.
    
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")
    
    # Checking if the stack has enough space.
    
    def has_space(self):
        return self.limit > self.size
    
    # Checking if the size of the stack is zero.
    
    def is_empty(self):
        return self.size == 0

# Defining an empty pizza stack.

pizza_stack = Stack(6)

# Adding pizzas as they are ready until we have.

pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Pushing a new pizza while there is no room left.

pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down.

print("The first pizza to deliver is " + pizza_stack.peek())

pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Trying to pop a pizza, while there's none left.

pizza_stack.pop()

print('\nThanks for reviewing')

# Thanks for reviewing 
