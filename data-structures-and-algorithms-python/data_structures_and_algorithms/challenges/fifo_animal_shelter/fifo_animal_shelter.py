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



class Stack :
    def __init__(self) :

        self.top = None
    def __str__(self):
        res = ""
        current = self.top
        while current:
            res += f"{ [current.value]} -> "
            current = current.next
        return res 

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
        """returns value at top of stack"""
        return self.top.value



class AnimalShelter : 

    def __init__(self):
        self.stck = Stack()
        self.temp = []


    def enqueue(self, animal):
        self.stck.push(animal)
        print(self.stck)


    def dequeue(self, pref):
        d= Dog.str_dog('d')
        c=Cat.str_cat('c')
        if pref == d or pref == c :
            while self.stck.peek() != pref :
                self.temp.append(self.stck.pop())
            an = self.stck.pop()
            while self.temp != [] :
                self.stck.push(self.temp[-1])
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