from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node : {self.value}'



class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        """takes in a value and adds it to the left of the root // end of line"""
        self.storage.appendleft(value)

    def dequeue(self):
        """removes Node from the front of queue // first in line"""
        return self.storage.pop()

    def peek(self):
        """returns value of Node at the front of queue // first in line"""
        return self.storage[-1]

    def is_empty(self):
        """returns bool if queue is empty"""
        return len(self.storage) == 0




class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """returns array of values ordered root, left, right"""
        output = []
        def walk(root): 
            """navigates tree"""
            if not root:
                return
            output.append(root.value)
            walk(root.left) 
            walk(root.right) 
        walk(self.root)
        return output

    def in_order(self):
        """returns array of values ordered left, root, right"""
        output = []
        def walk(node):
            """navigates tree"""
            if not node:
                return
            walk(node.left) 
            output.append(node.value) 
            walk(node.right) 
        walk(self.root)
        return output


    def post_order(self):
        """returns array of values ordered left, right, root"""
        output = []
        def walk(node):
            """navigates tree"""
            if not node:
                return
            walk(node.left) 
            walk(node.right)
            output.append(node.value) 
        return output

    def breadth_first(self):
        """returns list of Node values breadth first, from tree top to bottom left to right"""
        items = []
        breadth = Queue()
        if self.root == None : 
            raise ValueError ('empty tree')


        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            items.append(front.value)
            if front.left:
                breadth.enqueue(front.left)
            if front.right:
                breadth.enqueue(front.right)
        return items

class BinarySearchTree(BinaryTree):

    def add(self, value):
        """takes in a value, adds a new Node with that value to the correct location in binary search tree"""
        new_node = Node(value) 

        def walk_add(node, new):
            """navigates tree and adds new Node"""
            if not node:
                return
            if new_node.value < node.value: 
                if not node.left:
                    node.left = new_node
                else:
                    walk_add(node.left, new_node)
            else: 
                if not node.right:
                    node.right = new_node
                else:
                    walk_add(node.right, new_node)
        if not self.root:
            self.root = new_node
            return

        walk_add(self.root, new_node)

    def contains(self, value):
        """takes in a value, returns boolean if value is in tree"""
        if value in self.pre_order(): #returns list
            return True
        else:
            return False
