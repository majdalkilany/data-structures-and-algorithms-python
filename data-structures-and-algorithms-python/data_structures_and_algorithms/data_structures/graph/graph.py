
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

        adjacencies = self._adjacency_list[start_vertex] # list of neighbors
        adjacencies.append(edge)

    def get_vertex(self):

        return self._adjacency_list.keys()

   
    def get_neighbors(self, vertex):

        collection = []
        connections =  self._adjacency_list.get(vertex, [])         # <<<<<

        for neighbor in connections:
            holder = {}
            holder[neighbor] = neighbor.weight
            collection.append(holder)

        return collection

    def size(self):

        return len(self.graph) if len(self.graph) > 0 else None


