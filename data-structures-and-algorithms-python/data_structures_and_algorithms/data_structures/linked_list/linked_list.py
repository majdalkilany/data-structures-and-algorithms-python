class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += f"{ {str(current.value)} } ->"
            current = current.next
        return output


    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:

            new_node = Node(value)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def includes(self, values):
        current_node = self.head
        while current_node.next :

            if current_node.value == values:
                return True
            else:
                current_node = current_node.next
        return False



        # =================================4


    def insert_before(self,value,new_value):
        new_node = Node(new_value)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
                if current.value == value:
                    th_node = self.head
                    self.head = new_node
                    new_node.next = th_node
                    return 
                else:
                     current = self.head

                while current.next :
                    if current.next.value == value:
                        th_node = current.next
                        current.next = new_node
                        new_node.next = th_node
                        return 
                    else:
                        current = current.next

                return 








    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        if not self.head:
                self.head = new_node
        else:
            current = self.head
            while current.next != None:
                if current.next.value == value:
                    current = current.next
                    node_old = current.next
                    current.next = new_node
                    new_node.next = node_old
                    return 
                    
                else:
                    current = current.next
                    
            return



if __name__ == "__main__":
    ll =LinkedList()
    ll.append(4)
    print(ll)
    ll.append('mm')
    ll.insert_before(3,4)
    ll.insert_before('mm','d')
    ll.insert_before('d','mm')
    ll.insert_before(4,3)
    ll.insert_after('mm',44)
    ll.insert('f')
    ll.insert_after('f','majd')

    ll.append('d')
    mm = LinkedList()
    ll.append(4)
    print(ll)
    print(ll.includes(4))
