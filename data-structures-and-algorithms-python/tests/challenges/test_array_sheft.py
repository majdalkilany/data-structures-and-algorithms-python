from data_structures_and_algorithms.challenges.array_shift.array_sheft import array_sheft

def test() :
    expected = [3, 4, 5, 6, 8]
    actual = array_sheft([3,4,6,8],5)
    assert actual == expected