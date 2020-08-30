from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import Stack ,PseudoQueue 



def test_stack():
    assert Stack()

def test_PseudoQueue():
    assert PseudoQueue()


def test_dequeue():
    nums = PseudoQueue()
    nums.enqueue(1)
    actual = nums.dequeue()
    expected = 1
    assert actual == expected

def test_enqueue():
    nums = PseudoQueue()
    nums.enqueue(1)
    nums.enqueue(2)
    actual = nums.dequeue()
    expected = 1
    assert actual == expected



