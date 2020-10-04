import pytest
from collections import deque

from data_structures_and_algorithms.challenges.breadth_first_graph.breadth_first_graph import *
def test_node_graph():
    graph = Graph()
    node = graph.add_vertex('Test Node')
    actual = str(node)
    expected = 'Test Node'
    assert actual == expected

def test_add_edge_exception():
    with pytest.raises(KeyError):
        g1 = Graph()
        g2 = Graph()
        node1 = g1.add_vertex(1)
        node2 = g2.add_vertex(2)
        g1.add_edge(node1, node2)

def test_get_vertex():
    graph = Graph()
    node1 = graph.add_vertex(1)
    node2 = graph.add_vertex(2)
    actual = len(graph.get_vertex())
    expected = 2
    assert actual == expected

def test_get_edges_none():
    g = Graph()
    node_a = g.add_vertex('a')
    node_b = g.add_vertex('b')
    node_c = g.add_vertex('c')
    node_d = g.add_vertex('d')
    actual = g.get_edges(node_a)
    expected = []
    assert actual == expected

def test_get_edges_1():
    g = Graph()
    node_a = g.add_vertex('a')
    node_b = g.add_vertex('b')
    node_c = g.add_vertex('c')
    node_d = g.add_vertex('d')
    g.add_edge(node_a, node_b)
    actual = len(g.get_edges(node_a))
    expected = 1
    assert actual == expected

def test_size_none():
    g = Graph()
    actual = g.size()
    expected = None
    assert actual == expected

def test_size_1():
    g = Graph()
    g.add_vertex(1)
    actual = g.size()
    expected = 1
    assert actual == expected

def test_breadth_first_example():
    """ Refer to the README Examples for visual aids.
    """
    g = Graph()
    pandora = g.add_vertex('Pandora')
    adrendelle = g.add_vertex('Arendelle')
    metroville = g.add_vertex('Metroville')
    monstroplolis = g.add_vertex('Monstroplolis')
    naboo = g.add_vertex('Naboo')
    narnia = g.add_vertex('Narnia')
    g.add_edge(pandora, adrendelle)
    g.add_edge(adrendelle, metroville)
    g.add_edge(adrendelle, monstroplolis)
    g.add_edge(adrendelle, pandora)
    g.add_edge(metroville, adrendelle)
    g.add_edge(metroville, monstroplolis)
    g.add_edge(metroville, narnia)
    g.add_edge(metroville, naboo)
    g.add_edge(monstroplolis, adrendelle)
    g.add_edge(monstroplolis, metroville)
    g.add_edge(monstroplolis, naboo)
    g.add_edge(naboo, narnia)
    g.add_edge(naboo, metroville)
    g.add_edge(naboo, monstroplolis)
    actual = g.breadth_first(pandora)
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    assert actual == expected
