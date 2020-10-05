# In this program, we will create some functions which will allow a user to interactively play the
# game of the Hanoi Towers.

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

# Below, we create a class for stacks. More explanation on how these methods work is available at:
# https://github.com/kamyarpakdaman/ComputerScience-Mathematics/blob/master/Algorithms/basic_data_structures/stack.py

class Stack:
    
    def __init__(self, name):
        
        self.size = 0
        self.top_item = None
        self.limit = 1000
        self.name = name
  
    def push(self, value):

        if self.has_space():

            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        
        else:

            print("No more room!")

    def pop(self):
        
        if self.size > 0:

            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1

            return item_to_remove.get_value()
        
        print("This stack is totally empty.")

    def peek(self):
        
        if self.size > 0:
            
            return self.top_item.get_value()
        
        print("Nothing to see here!")

    def has_space(self):
        
        return self.limit > self.size

    def is_empty(self):
        
        return self.size == 0
    
    def get_size(self):
        
        return self.size
    
    def get_name(self):
        
        return self.name
  
    def print_items(self):

        pointer = self.top_item
        print_list = []

        while (pointer):

            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        
        print_list.reverse()
        print("{0} Stack: {1}".format(self.get_name(), print_list))

# Here, we start creating the game.

print("\nLet's play Towers of Hanoi!!")

# We create three stacks and put them in a list.

stacks = []

left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Here, we ask the user to input the number of disks, which should be greater thatn 3 to have a fun game. D:

num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

# We add the disks reversely to the left-most stack; such that they are sorted increasingly top to bottom.

for disk in range(num_disks, 0, -1):
    
    left_stack.push(disk)

# We know the optimal moves for solving the Hanoi Towers problem is 2^n - 1, where n is the number of disks.

num_optimal_moves = 2 ** num_disks - 1

print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))

# This function prompts the user for a disk number.

def get_input():

    choices = [stack.get_name()[0] for stack in stacks]

    while True:

        for i in range(len(stacks)):

            name = stacks[i].get_name()
            letter = choices[i]

            print('Enter {} for {}'.format(letter, name))
    
        user_input = input('')

        if user_input in choices:

            for i in range(len(choices)):
                
                if user_input == choices[i]:

                    return stacks[i]
        
# Below, the game actually starts. We use num_user_moves to track in how many moves the user can solve 
# the problem.

num_user_moves = 0

# The game prompts the user for moving disks in a valid way until the size of the right-most stack is
# equal to the number of disks.

while right_stack.get_size() < num_disks:
    
    print('\n\n\n...Current Stacks...')
    
    for stack in stacks:
    
        stack.print_items()
        
        # In the below while loop, the game ensures the user is making a valid move.

    while True:

        print("\nWhich stack do you want to move from?\n")
        
        from_stack = get_input()
        
        print("\nWhich stack do you want to move to?\n")
        
        to_stack = get_input()
        
        if from_stack.is_empty():
            
            print("\n\nInvalid Move. Try Again")
        
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            
            disk = from_stack.pop()
            
            to_stack.push(disk)
            
            num_user_moves += 1
            
            break
        
        else:
            
            print("\n\nInvalid Move. Try Again")

# Finally, we let the user know how good (s)he has been.

print("\n\nYou completed the game in {} moves, and the optimal number of moves is {}".format(num_user_moves, num_optimal_moves))

print('\nThanks for reviewing')

# Thanks for reviewing 
