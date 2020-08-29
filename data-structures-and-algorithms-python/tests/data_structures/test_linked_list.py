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



@pytest.mark.xfail(raises=TypeError)
def test_insert_no_value():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.insert() == "insert() missing 1 required positional argument: 'value' "


@pytest.mark.xfail(raises=TypeError)
def test_include_no_value():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes() == "TypeError: includes() missing 1 required positional argument: 'values' "



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


def test_LinkedList_kth_from():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(0)
    expected = 1
    assert actual == expected

def test_LinkedList_kth():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(2)
    expected = 8
    assert actual == expected

@pytest.mark.xfail(raises=IndexError)
def test_value_not_exists():
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual=ll.kth_from_end(4 )
    expected= IndexError
    assert actual==expected


def test_check_last_value():
    li=LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    expected=1   
    actual=li.kth_from_end(3)
    assert actual==expected

@pytest.mark.xfail(raises=ValueError)
def test_value_error() :
    ll=LinkedList()
    ll.append(2)
    ll.append(3)
    actual=ll.kth_from_end(-1)
    expected=ValueError      
    assert actual==expected

 

def test_linked_list_size_1():
    li=LinkedList()
    li.append(1)
    actual=li.kth_from_end(1)
    expected=1    
    assert actual==expected

def test_value_in_the_middle():
    li=LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    actual=li.kth_from_end(2)
    expected=1      
    assert actual==expected    
