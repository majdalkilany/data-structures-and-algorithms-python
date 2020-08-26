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

# def test_list_two_impty():
#     list1 = LinkedList()
#     list2 = LinkedList()
#     list1.insert("carrot")
#     list2.insert("1")
#     list1.insert("banana")
#     list2.insert("2")

#     list1.insert("apple")
#     list2.insert("3")
#     actual = str(zip_lists(list1, list2))
#     expected =  "{'carrot'} ->{'1'} ->{'banana'} ->{'2'} ->{'apple'} ->{'3'} ->"
#     assert actual == expected
