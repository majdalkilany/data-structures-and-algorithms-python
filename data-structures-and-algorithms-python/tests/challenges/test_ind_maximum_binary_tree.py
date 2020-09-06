from data_structures_and_algorithms.challenges.find_maximum_binary_tree.find_maximum_binary_tree import * 
import pytest



def test_1():
    bt = BinaryTree()
    bt.root= Node(1)
    bt.root.left = Node(110)
    bt.root.right = Node(51)
    assert bt.find_maximum_value() == 110

def test_2():
    bt = BinaryTree()
    bt.root= Node(-100)
    bt.root.left = Node(-123)
    bt.root.right = Node(-5)
    assert bt.find_maximum_value() == -5

def test_3():
    bt = BinaryTree()
    bt.root= Node(20)
    bt.root.left = Node(30)
    bt.root.right = Node(30)
    assert bt.find_maximum_value() == 30

def test_4():
    bt = BinaryTree()
    bt.root= Node(20)
    assert bt.find_maximum_value() == 20
@pytest.mark.xfail(raises=RuntimeError)
def test_5():
    bt = BinaryTree()
    assert bt.find_maximum_value() == 20
