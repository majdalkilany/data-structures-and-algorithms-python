from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import *

import pytest

def test_node():
    assert Node("test")

def test_stack():
    assert Stack()

def test_stack_push():
    push_1 = Stack()
    push_1.push(1)
    actual = push_1.peek()
    expected = 1
    assert actual == expected

def test_stack_push_two():
    st_test = Stack()
    st_test.push(1)
    st_test.push(2)
    actual = st_test.peek()
    expected = 2
    assert actual == expected

def test_stack_pop():
    st_test = Stack()
    st_test.push(1)
    st_test.push(2)
    actual = st_test.pop()
    expected = 2
    assert actual == expected

@pytest.mark.xfail(raises=TypeError)
def test_peek():
    stack = Stack()
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push()
    stack.push()
    stack.push()
    expected = stack.peek()

    assert expected == 'cannot pop an empty stack'

def test_stack_empty():
    nums = Stack()
    actual = nums.is_empty()
    expected = True


def test_queue_empty():
    nums = Queue()
    actual = nums.is_empty()
    expected = True

def test_enqueue():
    nums = Queue()
    nums.enqueue(1)
    nums.enqueue(2)
    actual = nums.peek()
    expected = 2

def test_dequeue():
    nums = Queue()
    nums.enqueue(1)
    actual = nums.dequeue()
    expected = 1
    assert actual == expected

