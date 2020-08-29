class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        '''
        this method to append value in the last node 

        input ==> value
        '''

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
        '''
        this method to adds an element to the list 

        input ==> element
        '''
                         
        if value is None:
            raise  TypeError("insert() missing 1 required positional argument: 'value' ") 
        

        else:

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


          '''
          this method to checks if an element 
          exists in the list and returns a boolean (True/Flase)

          input ==> value 
          output ==> boolean 
          '''
                         
          if values is None:
            raise  TypeError("includes() missing 1 required positional argument: 'values' ") 
          else:
            current_node = self.head
            while current_node.next :
                if current_node.value == values:
                    return True
                else:
                    current_node = current_node.next
            return False






        # =================================4


    def insert_before(self,value,new_value):
        '''
        adds an element to the list befor element  

        its take to element 
        first argument the value wich we will insert befor it 

        the second is the value wich we will insert 

        '''
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
        '''
        
        adds an element to the list after element  

        its take to element 
        first argument the value wich we will insert after it 

        the second is the value wich we will insert 
        
        
        '''

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





    def kth_from_end(self, k):
        """takes in a value(k) and returns the Node k places away from the tail"""
        current = self.head
        arr = []
        if k < 0:
            raise ValueError("value must be more than 0 ")
        while current:
            arr.append(current)
            current = current.next

        if len(arr) < k:
            raise IndexError("Value extends length of List.")

        arr.reverse()

        if k == len(arr):
            k = k -1
        return arr[k].value





# if __name__ == "__main__":
    # ll =LinkedList()
    # ll.append(4)
    # print(ll)
    # ll.append('mm')
    # ll.insert_aftere(3,4)
    # ll.insert_before('mm','d')
    # ll.insert_before('d','mm')
    # ll.insert_before(4,3)
    # ll.insert_after('mm',44)
    # ll.insert('f')
    # ll.insert_after('f','majd')

    # ll.append('d')
    # mm = LinkedList()
    # ll.append(4)
    # print(ll)
    # print(ll.includes(4))
    # print(ll.kth_from_end(3))

