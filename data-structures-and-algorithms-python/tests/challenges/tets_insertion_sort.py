from data_structures_and_algorithms.challenges.inseration_sort.inseartion_sort import * 

def test_insertion_sort():
    actual = insertion_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_insort_2():
    actual = insertion_sort([4, 3, 5, 2, 1])
    expected = [1, 2, 3, 4, 5]
    assert actual == expected

def test_insort_hundred():
    actual = insertion_sort([400, 300, 500, 200, 100])
    expected = [100, 200, 300, 400, 500]
    assert actual == expected

def test_insort_negative():
    actual = insertion_sort([-4, -3, -5, -2, -1])
    expected = [-5, -4, -3, -2, -1]
    assert actual == expected

