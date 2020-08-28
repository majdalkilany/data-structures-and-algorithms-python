from data_structures_and_algorithms.challenges.ll_zip.ll_zip import zip_lists 
from data_structures_and_algorithms.data_structures.linked_list.linked_list import Node ,LinkedList



def test_empty_list() :
      
    list1 = LinkedList()
    list2 = LinkedList()
    list1.insert("carrot")
    list1.insert("banana")
    list1.insert("apple")
    actual = str(zip_lists(list1, list2))
    expected = "{'carrot'} ->{'banana'} ->{'apple'} ->"
    assert actual == expected

def test_list_two_impty():
        list1 = LinkedList()
        list2 = LinkedList()
        list2.insert("carrot")
        list2.insert("banana")
        list2.insert("apple")
        actual = str(zip_lists(list1, list2))
        expected =  "{'carrot'} ->{'banana'} ->{'apple'} ->"
        assert actual == expected

def test_list_two():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.insert("carrot")
    list2.insert("1")
    list1.insert("banana")
    list2.insert("2")

    list1.insert("apple")
    list2.insert("3")
    actual = str(zip_lists(list1, list2))
    expected =  "{'carrot'} ->{'1'} ->{'banana'} ->{'2'} ->{'apple'} ->{'3'} ->"
    assert actual == expected

def test_zipLists2():
    list1 = LinkedList() 
    list2 = LinkedList() 
    list1.append(3) 
    list1.append(2) 
    list1.append(1) 
    list1.append(0) 
    list1.append(0) 
  
    list2.append(8) 
    list2.append(7) 
    list2.append(6)
    expected =  "{'3'} ->{'8'} ->{'2'} ->{'7'} ->{'1'} ->{'6'} ->{'0'} ->{'0'} ->"
    actual = str(zip_lists(list1, list2))
    assert actual == expected

def test_zipLists3():
    list1 = LinkedList() 
    list2 = LinkedList() 
    list1.append(3) 
    list1.append(2) 
    list1.append(1) 

  
    list2.append(8) 
    list2.append(7) 
    list2.append(6)
    list2.append(5) 
    list2.append(5)
    expected =  "{'3'} ->{'8'} ->{'2'} ->{'7'} ->{'1'} ->{'6'} ->{'5'} ->{'5'} ->"
    actual = str(zip_lists(list1, list2))
    assert actual == expected
