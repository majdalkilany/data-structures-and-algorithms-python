from data_structures_and_algorithms.data_structures.tree.tree import *
import pytest


def test_empty_binary_tree():
    bt = BinaryTree()
    assert bt.root == None

def test_pre_order_traverse(prepare_bt):
    actual = prepare_bt.pre_order()
    expected = [7, 13, 8, 9, 5, 1, -4]
    assert actual == expected

def test_bst_add_on_root():
    bst = BinarySearchTree()
    bst.add(4)
    expected = 4
    actual = bst.root.value
    assert actual == expected

def test_bst_add_4_values(prepare_bst):
    bst = prepare_bst
    bst = prepare_bst
    assert bst.root.value == 23
    assert bst.root.right.value == 42
    assert bst.root.left.value == 8
    assert bst.root.left.left.value == 4
    assert bst.root.right.left.value == 27
    assert bst.root.value == 23
    assert bst.root.right.value == 42
    assert bst.root.left.value == 8
    assert bst.root.left.left.value == 4
    assert bst.root.right.left.value == 27



@pytest.fixture
def prepare_bt():
    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(-4)
    return bt

@pytest.fixture
def prepare_bst():
    bst = BinarySearchTree()
    bst.add(23)
    bst.add(8)
    bst.add(4)
    bst.add(42)
    bst.add(27)
    return bst

def test_left_right():
    bst = BinarySearchTree()
    bst.add(2)
    bst.add(1)
    bst.add(3)
    right = bst.root.right.value
    expected_right = 3
    left = bst.root.left.value
    expected_left = 1
    assert right == expected_right
    assert left == expected_left

def test_pre():
    bst = BinarySearchTree()
    bst.add(1)
    bst.add(2)
    bst.add(3)
    bst.add(4)
    bst.add(5)
    actual = bst.pre_order()
    expected = [1, 2, 3, 4, 5]
    assert actual == expected

def test_in():
    bst = BinarySearchTree()
    bst.add(85)
    bst.add(70)
    bst.add(75)
    bst.add(45)
    bst.add(100)
    bst.add(90)
    bst.add(110)
    actual = bst.in_order()
    expected = [45, 70, 75, 85, 90, 100, 110]
    assert actual == expected

def test_post():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(60)
    bst.add(55)
    bst.add(40)
    bst.add(45)
    actual = bst.post_order()
    expected = [45, 40, 55, 60, 50]
    assert actual == expected

def test_contains():
    bst = BinarySearchTree()
    bst.add(1)
    bst.add(2)
    bst.add(3)
    actual = bst.contains(2)
    expected = True
    assert actual == expected
