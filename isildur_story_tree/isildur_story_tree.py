# In this program-or story, as we will see-, a user can go through the story of Isildur and Elrond
# in the history of the Middle Earth. We will use a tree data structure. At each level, the user
# can choose between two children of a parent tree node.

print('Once upon a time in Middle Earth. men and elves assembled their forces to defeat Sauron ...')

# Below, we create a tree class. More explanation on how these methods work can be found at:
# https://github.com/kamyarpakdaman/ComputerScience-Mathematics/blob/master/Algorithms/basic_data_structures/tree.py

class TreeNode:

    def __init__(self, story_piece):

        self.story_piece = story_piece
        self.choices = []
    
    def add_child(self, node):

        self.choices.append(node)
    
    # Through this method, we push the user to go forward in the story line.

    def traverse(self):

        story_node = self
        print(story_node.story_piece)

        # This loop ends when the user reaches one of the leaves of the tree.

        while len(story_node.choices) > 0:
            
            # The user is prompted to choose one of the two possible paths.

            choice = input('Enter 1 or 2 to continue the story: ')

            while choice not in ['1', '2']:

                print('Please enter 1 or 2!')
                
                choice = input('Enter 1 or 2 to continue the story: ')
            
            chosen_index = int(choice)
            chosen_index -= 1

            chosen_child = story_node.choices[chosen_index]

            print(chosen_child.story_piece)

            # The loop is closed and the user follows the path.

            story_node = chosen_child

root_str = """
You are Isildur. Sauron has been murdering people and capturing them for a while.
Elrond has asked for your help to march on Mordor's borders and defeat Sauron.
Do you decide to help him?

1. No way! Sauron has already got the ring. We had better escape.
2. Undoubtedly! For glory, and honor!
"""
story_root = TreeNode(root_str)

ch_a = """
To be honest, you have failed the people of Gondor. No one expected a heir of such
dynasty to be such a coward. A messenger from Rohan has come asking you last time for
help. Would you go and fight Sauron?

1. Just leave me alone! I'm on my way to western shores.
2. Ah OK! I will help them.
"""
choice_a = TreeNode(ch_a)

ch_b = """
Battle is about to begin. The army of Sauron is massive; however, the alliance are
terribly powerful as well. After hours of fighting hard, Sauron himself shows up. Such
a demon he is! He just killed your father. You reach his dead body and scream at Sauron's
face. He stretches his armoured hand to catch you. You have nothing to lose, and use your
# sword to attack him. Suddenly, something special happens. You cut his fingers and grab the
# ring. Sauron vanishes and his army defeat leaderless. Elrond comes to you and asks you
# to move to the Mount Doom to destroy the ring for good. Will you go with him?

1. Sure thing! Let's get rid of this damn ring of devilry stuff.
2. No! It's my precious.
"""
choice_b = TreeNode(ch_b)

story_root.add_child(choice_a)
story_root.add_child(choice_b)

ch_a_1 = """
Just go west and never comeback man!

End of the story.
"""
choice_a_1 = TreeNode(ch_a_1)

ch_a_2 = """
Great! You join forces with Elrond and all free folk against Sauron and defeat him mysteriously.

End of the story.
"""
choice_a_2 = TreeNode(ch_a_2)

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

ch_b_1 = """
I wish you had stayed on your word. Unfortunately, later on you betray Elrond and decide to own the
ring. Such a mistake. Isildur finally paid with his life for this mistake.

End of the story.
"""
choice_b_1 = TreeNode(ch_b_1)

ch_b_2 = """
Just have it. It will cost your life, but it's OK.

End of the story.
"""
choice_b_2 = TreeNode(ch_b_2)

choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

story_root.traverse()

print('\nThanks for reviewing')

# Thanks for reviewing
