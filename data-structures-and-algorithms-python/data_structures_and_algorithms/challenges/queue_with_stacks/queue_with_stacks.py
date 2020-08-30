from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack ,Node

class PseudoQueue : 

    def __init__ (self) :
            
        self.stck_1 = Stack()
        self.stck_2 = Stack()
    def enqueue ( self , value) :
        '''
        take value and put it in the node on the back of the stack
        '''
        self.stck_1.push(value)

    def dequeue (self) : 
        

        while not self.stck_1.is_empty() : 
            self.stck_2.push(self.stck_1.pop())

        if self.stck_2.is_empty ( ) :
            raise RuntimeError('cannot dequeue  from empty stack!!') 

        return self.stck_2.pop()



if __name__ == "__main__":
    majd =   PseudoQueue()
    majd.enqueue(3)          
    majd.enqueue(4)          
    majd.enqueue(5)   
    print(majd)    
    assert majd =='[10]->[15]->[20]->'
    print('done')

