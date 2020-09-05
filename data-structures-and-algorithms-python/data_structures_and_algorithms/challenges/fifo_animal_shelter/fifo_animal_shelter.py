class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Dog : 
    def __init__(self , name) :
        self.name = name 

    def __str__(self):
        return 'dog'



class Cat : 
    def __init__(self , name) :
        self.name = name 

    def __str__(self):
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
        self.queue_dogs = Queue()
        self.queue_cats = Queue()
        self.not_animal = []



    def enqueue(self, animal):
        '''
        to add cat or dog to shelter
        '''
        if  animal.__str__() == 'dog' :
             self.queue_dogs.enqueue(animal) 
        elif  animal.__str__() == 'cat' :
             self.queue_cats.enqueue(animal) 
        else :
             return 'the input must be cat or dog'

        self.not_animal.append(animal)

    def dequeue(self, pref):
        '''
        to remove cat or dog from shelter
        '''


        dog_1= Dog('dog_1')
        cat_1=Cat('dog_1')
        if  pref.__str__() == 'dog' :
              return self.queue_dogs.dequeue() 
        elif  pref.__str__() == 'cat' :
              return self.queue_cats.dequeue() 
        else :
                return None

    def __str__(self):
        res = ""
        current = self._front
        while current:
            res += f"{ [current.value]} -> "
            current = current.next
        return res 


        # if pref == d or pref == c :
        #     while self.stck.peek() != pref :
        #         self.temp.append(self.stck.pop())
        #     an = self.stck.pop()
        #     while self.temp != [] :
        #         self.stck.push(self.temp[-1])
        #     print(self.stck)
        #     return an 
        # else : 
        #     return None











if __name__ == "__main__":
    meme = Cat('meme')
    print(meme.__str__())
    print(isinstance(meme, Cat))
    oscar = Dog('oscar')
    print(oscar.__str__())
    ll = AnimalShelter()
    ll.enqueue(oscar)
    ll.enqueue(meme)
    print(ll)
    m = Dog('m')
    v = Dog('v')
    r = Dog('r')
    ll.enqueue(m)
    ll.enqueue(v)
    ll.enqueue(r)
    print(ll)
    # ll.dequeue('cat')