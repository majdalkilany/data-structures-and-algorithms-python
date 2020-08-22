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


if __name__ == "__main__":
    ll =LinkedList()
    ll.append(4)
    print(ll)
    ll.append('mm')
    ll.insert('m')
    ll.insert('f')
    ll.append('d')
    mm = LinkedList()
    ll.append(4)
    print(ll)
    print(ll.includes(4))
