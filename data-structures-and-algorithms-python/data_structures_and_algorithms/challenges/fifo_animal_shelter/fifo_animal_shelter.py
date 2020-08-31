class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Dog : 
    def __init__(self , name) :
        self.name = name 

    def __str__(self):
        return f'{self.name}'
    def str_dog(self) :
        return 'dog'



class Cat : 
    def __init__(self , name) :
        self.name = name 

    def __str__(self):
        return f'{self.name}'
    def str_cat(self) :
        return 'cat'


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


    def __str__(self):
        res = ""
        current = self._front
        while current:
            res += f"{ [current.value]} -> "
            current = current.next
        return res 



class AnimalShelter : 

    def __init__(self):
        self.stck = Queue()
        self.temp = []


    def enqueue(self, animal):
        self.stck.enqueue(animal)
        print(self.stck)


    def dequeue(self, pref):
        d= Dog.str_dog('d')
        c=Cat.str_cat('c')
        if pref == d or pref == c :
            while self.stck.peek() != pref :
                self.temp.append(self.stck.dequeue())
            an = self.stck.dequeue()
            while self.temp != [] :
                self.stck.enqueue(self.temp[-1])
            print(self.stck)
            return an 
        else : 
            return None











if __name__ == "__main__":
    meme = Cat('meme')
    print(meme.str_cat())
    print(isinstance(meme, Cat))
    oscar = Dog('oscar')
    print(oscar.str_dog())
    ll = AnimalShelter()
    ll.enqueue(oscar)
    ll.enqueue(meme)
    # print(ll)
    m = Dog('m')
    v = Dog('v')
    r = Dog('r')
    ll.enqueue(m)
    ll.enqueue(v)
    ll.enqueue(r)
    
    # ll.dequeue('cat')