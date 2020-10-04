from collections import deque

class Vertex:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def __len__(self):
        return len(self._adjacency_list)

    def add_vertex(self, value):
        v = Vertex(value)
        self._adjacency_list[v] = [] 
        return v

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list:
            raise KeyError('start vertex not in graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('end vertex not in graph')


        edge = Edge(end_vertex, weight)

        adjacencies = self._adjacency_list[start_vertex] 
        adjacencies.append(edge)


    def get_vertex(self):
        return self._adjacency_list.keys()

    def get_edges(self, vertex):
        return self._adjacency_list.get(vertex, [])

    def size(self):
        return len(self._adjacency_list) if len(self._adjacency_list) > 0 else None

    def breadth_first(self, vertex):
        nodes = []
        holder = set()
        breadth = Queue()                  
        holder.add(vertex.value)          
        breadth.enqueue(vertex)            
        while not breadth.is_empty():      
            front = breadth.dequeue()      
            nodes.append(front.value)     

            for child in self._adjacency_list[front]:       
                if child.vertex.value not in holder:        
                    holder.add(child.vertex.value)
                    breadth.enqueue(child.vertex)

        return nodes



class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0
