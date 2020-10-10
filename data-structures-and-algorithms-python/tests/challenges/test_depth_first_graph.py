import pytest
from data_structures_and_algorithms.challenges.depth_first_graph.depth_first_graph import *
def test_example_input1():
    my_graph = Graph()
    a = my_graph.add_vertex("A")
    b = my_graph.add_vertex("B")
    c = my_graph.add_vertex("C")
    d = my_graph.add_vertex("D")
    e = my_graph.add_vertex("E")
    f = my_graph.add_vertex("F")
    g = my_graph.add_vertex("G")
    h = my_graph.add_vertex("H")
    my_graph.add_edge(a, b)
    my_graph.add_edge(a, d)

    my_graph.add_edge(b, c)
    my_graph.add_edge(b, d)

    my_graph.add_edge(c, g)

    my_graph.add_edge(d, e)
    my_graph.add_edge(d, h)
    my_graph.add_edge(d, f)
    my_graph.add_edge(d, b)

    actual = depth_first(my_graph, a)
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert actual == expected

def test_example_input2():
    my_graph = Graph()
    a = my_graph.add_vertex("A")
    b = my_graph.add_vertex("B")
    c = my_graph.add_vertex("C")
    d = my_graph.add_vertex("D")
    e = my_graph.add_vertex("E")
    f = my_graph.add_vertex("F")
    g = my_graph.add_vertex("G")
    h = my_graph.add_vertex("H")
    my_graph.add_edge(a, b)
    my_graph.add_edge(a, d)

    my_graph.add_edge(b, c)
    my_graph.add_edge(b, d)

    my_graph.add_edge(c, g)

    my_graph.add_edge(d, e)
    my_graph.add_edge(d, h)
    my_graph.add_edge(d, f)
    my_graph.add_edge(d, b)
    my_graph.add_edge(d, a)

    my_graph.add_edge(h, f)

    actual = depth_first(my_graph, b)
    expected = ['B', 'C', 'G', 'D', 'E', 'H', 'F', 'A']
    assert actual == expected
