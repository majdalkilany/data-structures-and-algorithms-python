from data_structures_and_algorithms.challenges.fizzBuzzTree.fizz_buzz_tree import *

import pytest



def test_BinaryTree_breadth():
    tree = BinaryTree()
    tree.add(1)
    tree.add(5)
    tree.add(4)
    tree.add(7)
    actual = tree.breadth_first()
    expected = [1, 5, 4, 7]
    assert actual == expected


def test_fizz_buzz_tree():
    tree = BinaryTree()
    tree.add(1)
    tree.add(5)
    tree.add(4)
    tree.add(7)
    new_tree = fizz_buzz_tree(tree)
    actual = new_tree.breadth_first()
    expected = ['1', 'Buzz', '4', '7']
    assert actual == expected


def test_fizz_buzz_tree_2():
    tree = BinaryTree()
    tree.add(3)
    tree.add(15)
    tree.add(7)
    tree.add(5)
    tree.add(3)
    tree.add(5)
    tree.add(15)
    new_tree = fizz_buzz_tree(tree)
    actual = new_tree.breadth_first()
    expected = ['Fizz', 'FizzBuzz', '7', 'Buzz', 'Fizz', 'Buzz', 'FizzBuzz']
    assert actual == expected


def test_fizz_buzz_tree_fizz():
    tree = BinaryTree()
    tree.add(3)
    tree.add(9)
    tree.add(6)
    tree.add(12)
    new_tree = fizz_buzz_tree(tree)
    actual = new_tree.breadth_first()
    expected = ['Fizz', 'Fizz', 'Fizz', 'Fizz']
    assert actual == expected

def test_fizz_buzz_tree_buzz():
    tree = BinaryTree()
    tree.add(5)
    tree.add(10)
    tree.add(25)
    tree.add(20)
    new_tree = fizz_buzz_tree(tree)
    actual = new_tree.breadth_first()
    expected = ['Buzz', 'Buzz', 'Buzz', 'Buzz']
    assert actual == expected

def 
