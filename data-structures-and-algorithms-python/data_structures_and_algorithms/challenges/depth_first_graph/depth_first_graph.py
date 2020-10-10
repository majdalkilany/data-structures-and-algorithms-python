class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class Stack:
    def __init__(self, item=None):
        self.top = item

    def push(self, item):
        if self.top == None:
            self.top = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            raise AttributeError("Can't pop item for an empty stack")
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.value

    def peek(self):
        if not self.top:
            raise AttributeError("Can't peek top from an empty stack")
        return self.top.value

    def is_empty(self):
        return not bool(self.top)

def depth_first(graph, root):
    storage = Stack()
    visited = []

    storage.push(root)
    visited.append(root.value)

    while not storage.is_empty():

        top = storage.peek()
        status = False

        for child in graph._adjacency_list[top]:

            if child.vertex.value not in visited:
                status = True
                storage.push(child.vertex)
                visited.append(child.vertex.value)
                break

        if status:
            continue
        else:
            storage.pop()

    return visited







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

    #   get node
    def get_vertex(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        collection = []
        connections =  self._adjacency_list.get(vertex, [])         

        for neighbor in connections:
            holder = {}
            holder[neighbor] = neighbor.weight
            collection.append(holder)

        return collection

    def size(self):
        return len(self.graph) if len(self.graph) > 0 else None


    def breadth_first(self, vertex):
        nodes = []
        holder = set()
        breadth = Queue()
        holder.add(vertex.value)
        breadth.enqueue(vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            nodes.append(front.value)

            for child in self.graph[front]:
                if child.vertex.value not in holder:
                    holder.add(child.vertex.value)
                    breadth.enqueue(child.vertex)

        return nodes
