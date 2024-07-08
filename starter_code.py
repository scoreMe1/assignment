# Problem Statement:
# You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
# The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
# representing an edge from node `i` to node `j` with weight `w`.
# Your task is to find the longest path in the graph starting from any node.

def longest_path(graph: list) -> int:
    # Your implementation goes here
    pass

# Helper function to perform topological sort
def topological_sort(graph):
    # Your implementation goes here
    pass

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    # Your implementation goes here
    pass

# Test cases
def test_longest_path():
    graph1 = [
        [(1, 3), (2, 2)],
        [(3, 4)],
        [(3, 1)],
        []
    ]
    assert longest_path(graph1) == 7

    graph2 = [
        [(1, 2), (2, 1)],
        [(3, 1)],
        [(3, 5)],
        []
    ]
    assert longest_path(graph2) == 6

    graph3 = [
        [(1, 10)],
        [(2, 10)],
        [(3, 10)],
        []
    ]
    assert longest_path(graph3) == 30

    graph4 = [
        [(1, 1), (2, 1)],
        [(3, 1)],
        [(3, 1)],
        []
    ]
    assert longest_path(graph4) == 3

    print("All test cases pass")

# Uncomment the line below to run the tests
# test_longest_path()
