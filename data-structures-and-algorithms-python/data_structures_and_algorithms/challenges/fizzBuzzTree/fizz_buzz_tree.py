from data_structures_and_algorithms.challenges.breadth_first.breadth_first import *

def fizz_buzz_tree(tree):
    """Takes in a tree as a single argument. Changes values 
    to fizz and buzz 
    
    """
    collection = tree.breadth_first()
    new_collection = []

    for i in collection:
        if i % 3 == 0 and i % 5 == 0:
            i = 'FizzBuzz'
            new_collection.append(i)
        elif i % 3 == 0:
            i = 'Fizz'
            new_collection.append(i)
        elif i % 5 == 0:
            i = 'Buzz'
            new_collection.append(i)
        else:
            i = str(i)
            new_collection.append(i)

    new_tree = BinaryTree()

    for i in new_collection:
        new_tree.add(i)

    return new_tree


