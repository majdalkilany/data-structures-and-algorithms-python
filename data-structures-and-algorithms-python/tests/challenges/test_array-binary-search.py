from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import *
    
def test_1 () :
    expected =3
    actual = array_binary_search(4,[1,2,3,4,5,6,7,8,9,10,11,12])
    assert actual==expected
def test_3 () :
    expected ='the value is not in the list '
    actual = array_binary_search(50,[1,2,3,4,5,6,7,8,9,10,11,12])
    assert actual==expected
def test_2 () :
    arr = []
    for i in range(1000000):
        arr.append(i)
    expected =49
    actual = array_binary_search(49,arr)
    assert actual==expected
def test_5 () :
    arr = []
    for i in range(1000000):
        arr.append(i)
    expected =1
    actual = array_binary_search(1,arr)
    assert actual==expected

def test_5 () :
    arr = []
    for i in range(1000000):
        arr.append(i)
    expected =999
    actual = array_binary_search(999,arr)
    assert actual==expected
