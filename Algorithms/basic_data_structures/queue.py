# In this program, we will define a class for nodes and then create a
# class for queues with some capabilities. Then we will handle the queue
# in a restaurant.

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

# Defining a class for queues.

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    
    # By using the enqueue() mehtod, we add a new node to the end of the
    # queue. If the queue is empty, this node will be both the head and the
    # tail of the queue. Further, should the queue has no space, no new
    # node can be added to it.

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")
    
    # By using the dequeue() mehtod, we return the value of the head of the
    # queue and then omit it from the queue. Further, should the queue has no
    # nodes, no head node can be retrieved.
     
    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print(str(item_to_remove.get_value()) + " is served!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is totally empty!")
    
    # Similar to dequeue(), except that we just return the value of the head
    # node, but don't remove it from the queue.

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("No orders waiting!")

    # Retrieving the size of the queue.

    def get_size(self):
        return self.size
  
    # Checking if the queue has free space and returning a logical value.

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    # Checking if the queue is empty and returning a logical value.

    def is_empty(self):
        return self.size == 0

# Adding ten items to the queue of the orders in a restaurant.

print("Creating a deli line with up to 10 orders ...\n")
deli_line = Queue(10)
print("Adding orders to our deli line ...\n")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")

# Adding an item to the queue that exceeds the limit.

deli_line.enqueue("western omelet with home fries")

print("\nOur first order will be " + deli_line.peek())
print("\nNow serving ...\n")

# Serving some orders

deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()

# Trying to serve a new order, while none exists.

deli_line.dequeue()

print('\nThanks for reviewing')

# Thanks for reviewing 
