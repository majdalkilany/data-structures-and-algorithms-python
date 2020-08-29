from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList ,Node

def zip_lists( list1, list2):
    """takes two linked lists and merges them starting with head1 then head2"""

    if not list1 :
        return list1 
    if not list2 :
        return list1 
    output =LinkedList()
    current1 =list1.head
    current2 =list2.head
    while current1 :
        output.append(current1.value)
        if current2 :
            output.append(current2.value)
            current2 = current2.next
        current1= current1.next
    while current2 :
        output.append(current2.value)
        current2 =current2.next
    return output



if __name__ == "__main__":
    majd = LinkedList()
    majd.append(1)
    majd.append(2)
    ahmad = LinkedList()
    ahmad.append(5)
    ahmad.append(10)
    
