from data_structures_and_algorithms.challenges.breadth_first.breadth_first import BinaryTree , BinarySearchTree ,Node
import pytest
def test_1():
    bt = BinaryTree()
    bt.root = Node(1)

    bt.root.left = Node(2)  
    bt.root.right = Node(3)  

    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.left.right.left = Node(7)  
    bt.root.left.right.right = Node(8)  


    bt.root.right.right = Node(6)
    bt.root.right.right.left = Node(9) 
    breadth_first = bt.breadth_first()
    assert breadth_first == [1,2,3,4,5,6,7,8,9]

def test_3():
    bt = BinaryTree()
    bt.root = Node(1)

    bt.root.left = Node(2)  
    bt.root.right = Node(3)  

    assert bt.breadth_first() == [1, 2, 3]
def test_2():
    bt = BinaryTree()
    bt.root = Node(1)

    bt.root.left = Node(2)  
    bt.root.right = Node(3)  


    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)


    assert bt.breadth_first() == [1, 2, 3,4,5]


@pytest.mark.xfail(raises=ValueError)
def test_4():
    bt = BinaryTree()


    assert bt.breadth_first() == ''
