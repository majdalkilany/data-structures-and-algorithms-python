
import pytest

from data_structures_and_algorithms.data_structures.hash_tables.hash_tables import Hashmap , Node , LinkedList

def test_hash_key():
    myHash = Hashmap(10)
    actual = myHash.hash('a')
    expected = 3
    assert actual == expected

def test_add_to_hashtable():
    myHash = Hashmap(3)
    myHash.add('one item', 1)
    actual = myHash.contains('one item')
    expected = True
    assert actual == expected

def test_get_key():
    myHash = Hashmap(100)
    myHash.add('something', 10)
    myHash.add('random', 42)
    myHash.add('code', 99)
    actual = myHash.get('random')
    expected = 42
    assert actual == expected

def test_retrieve_from_bucket():
    myHash = Hashmap(100)
    myHash.add('random', 10)
    myHash.add('rnadom', 42)
    actual1 = myHash.get('random')
    actual2 = myHash.get('rnadom')
    expected = [10, 42]
    assert [actual1, actual2] == expected

def test_get_key_invalid():
    myHash = Hashmap(100)
    myHash.add('something', 10)
    myHash.add('random', 42)
    myHash.add('code', 99)
    actual = myHash.get('FooBar!')
    expected = None
    assert actual == expected