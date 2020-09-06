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
        walk(self.root)
        return output

    def find_maximum_value (self) : 
        '''
        to find max value in tree
        '''
        output = []
        def walk(node):
            """navigates tree"""
            if not node:
                return
            walk(node.left) 
            output.append(node.value) 
            walk(node.right) 
        walk(self.root)
        max_val = None    #initial value for max 
        for i in output : 
            if not max_val : 
                max_val = i

            if i  > max_val : 
              max_val = i 
        if max_val == None : 
            raise RuntimeError ('empty tree')
        return max_val





            #   this to try find max whith recurtion 

        # def walk(node):
        #     if not node:
        #         return
        #     res = node
        #     l_res =  walk(node.left) 
        #     r_res = walk(node.right) 
        #     if l_res > r_res : 
        #         res = l_res 
        #     if r_res > l_res : 
        #         res = r_res 
        #     return res 


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(-4)
    print(bt.find_maximum_value())
    print(bt.post_order())