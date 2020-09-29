from data_structures_and_algorithms.challenges.left_join.left_join import *
import pytest

def test_left_join():
    hashmap1 = {
        'fond' : 'enamored',
        'wrath' : 'anger',
    }

    hashmap2 = {
        'fond' : 'averse',
        'wrath' : 'delight',
    }

    actual = left_join(hashmap1, hashmap2)
    expected = [
        ['fond', 'enamored', 'averse'],
        ['wrath', 'anger', 'delight'],
    ]
    assert actual == expected

def test_left_join_none():
    hashmap1 = {
        'fond' : 'enamored',
        'food' : 'yummy',
        'diligent' : 'employed',
        'guide' : 'usher',
        'flow' : 'boom',
        'computer' : 'network',
    }

    hashmap2 = {
        'random': 'something',
        'fond' : 'averse',
        'wrath' : 'delight',
        'diligent' : 'idle',
        'guide' : 'follow',
        'flow' : 'jam',
    }

    actual = left_join(hashmap1, hashmap2)
    expected = [
        ['fond', 'enamored', 'averse'],
        ['food', 'yummy', None],
        ['diligent', 'employed', 'idle'],
        ['guide', 'usher', 'follow'],
        ['flow', 'boom', 'jam'],
        ['computer', 'network', None]
    ]

    assert actual == expected
