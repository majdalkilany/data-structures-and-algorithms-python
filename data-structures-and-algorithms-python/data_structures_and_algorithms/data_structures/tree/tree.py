class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        output = []
        def _walk(node):
            if not node:
                raise 'empty tree'
                return
            output.append(node.value)
            _walk(node.left)
            _walk(node.right)

        _walk(self.root)
        return output



    def in_order(self):
        """returns array of values ordered left, root, right"""
        output = []
        def walk(node):
            """navigates tree"""
            if not node:
                return
            walk(node.left) # check left
            output.append(node.value) # root
            walk(node.right) # check right
        walk(self.root)
        return output


    def post_order(self):
        """returns array of values ordered left, right, root"""
        output = []
        def walk(node):
            """navigates tree"""
            if not node:
                return
            walk(node.left) # check left
            walk(node.right) # check right
            output.append(node.value) # root
        walk(self.root)
        return output
class BinarySearchTree(BinaryTree):
    def add(self, value):

        '''
        add value to binery tree 
        '''
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while (current):
                if current.value > value: 
                    if current.left == None: 
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None: 
                        current.right = Node(value)
                        break
                    current = current.right
    def contains(self, value):
        """check value in """
         if self._root == None:
            raise "its empty tree "


        if value in self.pre_order(): 
            return True
        else:
            return False
if __name__ == "__main__":
