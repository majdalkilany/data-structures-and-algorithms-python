import pytest
from data_structures_and_algorithms.challenges.repeated_word.repeated_word import repeat_word

def test_repeat_word():
    test = 'i like winter but winter is very cold this year '
    actual = repeat_word(test)
    expected = 'winter'
    assert actual == expected

def test_repeat_word_non():
    test = 'we will be there on the time '
    actual = repeat_word(test)
    expected = None
    assert actual == expected

def test_repeat_word_capt():
    test = "THE WEATHER IS VERY HOT AND THE AC DOESN'T WORK "
    actual = repeat_word(test)
    expected = 'THE'
    assert actual == expected


def test_repeat_word__():
    test = ' i like this song but i did not like the singer'
    actual = repeat_word(test)
    expected = 'i'
    assert actual == expected
