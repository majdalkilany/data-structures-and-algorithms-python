class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack :
    def __init__(self) :

        self.top = None
    def __str__(self):
        res = ""
        current = self.top
        while current:
            res += f"{ [current.value]} -> "
            current = current.next
        return res + "NULL"

    def push (self,value) : 
        '''
        it takes one value as argument and push it to the top of the stack
        '''

        if self.top == None : 
            self.top = Node(value)
        else :
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node




    def is_empty(self) :
        '''
            returns boolen if the stack is empty or not
        '''

        return self.top is None 




    def pop(self):
        """removes node on top of stack and returns that value"""
        if not self.top:
            raise Exception('cannot pop an empty stack')

        if self.top:
            outgoing = self.top
            self.top = self.top.next
            return outgoing.value



    def peek(self):
        '''
        return the first node value of the top of the stack:
            output >> the top value of the stack
        '''
        try:
            return self.top.value
        except TypeError:
            return "stack is empty"




class Queue:
    def __init__(self):
        self._front = None
        self._rear = None

    def enqueue(self, value):
        """add new value to front of linked list"""
        node = Node(value)

        if self._rear: 
            self._rear.next = node
            self._rear = node

        else:
            self._rear = self._front = node

    def dequeue(self):
        """removes node from linked list"""
        if not self._front:
            raise Exception('cannot dequeue an empty stack')

        exiting = self._front
        self._front = self._front.next
        return exiting.value

    def peek(self):
        """returns front Node vlaue, first in line"""
        if not self._front:
            raise Exception('cannot peek an empty stack')

        return self._front.value

    def is_empty(self):
        """returns bool if queue is empty"""
        return not self._front 

if __name__ == "__main__":
    majd = Stack()
    # majd.push(5)
    # majd.push(6)
    # majd.push(7)
    # majd.pop()
    # majd.push(6)
    # print(majd.is_empty())
    # print(majd.peek())    