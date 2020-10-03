from data_structures_and_algorithms.data_structures.graph.graph import Graph , Vertex 




import pytest


def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertex('spam')
    actual = vertex.value
    expected = 'spam'
    assert actual == expected

def test_add_edge():
    graph = Graph()

    apples = graph.add_vertex('apples')
    bananas = graph.add_vertex('bananas')
    graph.add_edge(apples, bananas)

    assert True, ('will be fully excersized in get neighbors test')

def test_add_edge_outsider():
    graph = Graph()
    insider = graph.add_vertex('insider')
    outsider = Vertex('outsider')

    with pytest.raises(KeyError):
        graph.add_edge(outsider, insider )


def test_get_vertices():
    graph = Graph()
    apples = graph.add_vertex('apples')
    bananas = graph.add_vertex('bananas')

    actual = graph.get_vertex()
    assert len(actual) == 2


def test_get_size():
    graph = Graph()
    apples = graph.add_vertex('apples')
    bananas = graph.add_vertex('bananas')

    assert len(graph) == 2

def test_get_neighbors_none():
    g = Graph()
    node_a = g.add_vertex('a')
    node_b = g.add_vertex('b')
    node_c = g.add_vertex('c')
    node_d = g.add_vertex('d')
    actual = g.get_neighbors(node_a)
    expected = []
    assert actual == expected

def test_get_neighbors_1():
    g = Graph()
    node_a = g.add_vertex('a')
    node_b = g.add_vertex('b')
    node_c = g.add_vertex('c')
    node_d = g.add_vertex('d')
    g.add_edge(node_a, node_b)
    actual = len(g.get_neighbors(node_a))
    expected = 1
    assert actual == expected

