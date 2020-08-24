from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)

import pytest



def test_instance():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)

    assert isinstance(ll, LinkedList)

def append() : 
    m_m=LinkedList
    m_m.append(2)
    m_m.append(3)
    m_m.append(4)
    acepted = "{'2'} ->{'3'} ->{'4'} ->"
    actual = m_m()


def test_insert():


    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)


    result = ''
    linked_list = ll.head
    while linked_list:
        result += f'{linked_list.value},'
        linked_list = linked_list.next
    assert result == '1,2,3,'

def test_fisrt_elment():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.head.value == 1

def test_false_value():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(5) == False

def test_true():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(2) == True

def test_str():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.__str__() == "{'1'} ->{'2'} ->{'3'} ->"




def test_insert_before():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert_before(2,3)
    assert ll.__str__() == "{'1'} ->{'3'} ->{'2'} ->"



def test_insert_before_head():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.insert_before(5,4)
    assert ll.__str__() == "{'4'} ->{'5'} ->{'6'} ->"


def test_insert_after_the_last_one():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3,4)
    assert ll.__str__() == "{'1'} ->{'2'} ->{'3'} ->{'4'} ->"

def test_insert_after():
    ll = LinkedList()
    ll.insert(5)
    ll.append(6)
    ll.insert_after(6,8)
    ll.insert(7)
    assert ll.__str__() == "{'5'} ->{'6'} ->{'8'} ->{'7'} ->"
