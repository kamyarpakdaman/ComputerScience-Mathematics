# In this program, we are going to implement a hash map to relate the names of flowers to their 
# meanings. In order to avoid collisions when our hashing function collides the names of two flowers, 
# we are going to use separate chaining. We will implement the Linked List data structure for each
# of these separate chains.

# At first, we create two classes of Node and LinkedList for later use. For more explanation on what
# these classes and their methods do (plust the hashmap class), please visit:
# https://github.com/kamyarpakdaman/ComputerScience-Mathematics/blob/master/Algorithms/basic_data_structures/linked_list.py
# https://github.com/kamyarpakdaman/ComputerScience-Mathematics/blob/master/Algorithms/basic_data_structures/hash_map.py

class Node:
    
    def __init__(self, value):
        
        self.value = value
        self.next_node = None
    
    def get_value(self):
        
        return self.value
  
    def get_next_node(self):

        return self.next_node
  
    def set_next_node(self, next_node):
        
        self.next_node = next_node

class LinkedList:
    
    def __init__(self, head_node=None):
        
        self.head_node = head_node
  
    def insert(self, new_node):
        
        current_node = self.head_node

        if not current_node:
        
            self.head_node = new_node

        while(current_node):
            
            next_node = current_node.get_next_node()
            
            if not next_node:
                
                current_node.set_next_node(new_node)
        
            current_node = next_node

    def __iter__(self):
        
        current_node = self.head_node
        
        while(current_node):
            
            yield current_node.get_value()
            current_node = current_node.get_next_node()

# In the first step, we create our HashMap class.

class HashMap:

    def __init__(self, size):

        self.array_size = size
        self.array = [LinkedList() for i in range(size)]
    
    # This method is used to hash the input string.

    def hash(self, key):

        return sum(key.encode())
    
    # The compress method is used to scale a hash code into the HashMap array size.

    def compress(self, hash_code):

        return hash_code % self.array_size
    
    # Below method is used for assigning a new pair of key, values to the hashmap.

    def assign(self, key, value):
    
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_index = self.array[array_index]
        
        for item in list_at_index:

            if item[0] == key:

                item[1] = value

                return
            
            else:

              continue
        
        list_at_index.insert(payload)
    
    # Below method returns the value for a given key in the hashmap.

    def retrieve(self, key):
    
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]

        for item in list_at_index:
            
            if item[0] == key:

                print(item[1])
                
                return item[1]
            
            return None

# Now, let's add some flower definitions to a hashmap.

flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 'cheerfulness'], ['carnation', 'memories'], 
['daisy', 'innocence'], ['hyacinth', 'playfulness'], ['lavender', 'devotion'], ['magnolia', 'dignity'], 
['morning glory', 'unrequited love'], ['periwinkle', 'new friendship'], ['poppy', 'rest'], ['rose', 'love'], 
['snapdragon', 'grace'], ['sunflower', 'longevity'], ['wisteria', 'good luck']]

blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:

    blossom.assign(flower[0], flower[1])

# Finally, let's use our hashmap.

blossom.retrieve('daisy')

print('\nThanks for reviewing')

# Thanks for reviewing  
