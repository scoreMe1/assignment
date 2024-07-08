Problem Statement: Longest Path in a Weighted Directed Acyclic Graph (DAG)
Problem Description

You are given a Directed Acyclic Graph (DAG) with n nodes, numbered from 0 to n-1. The graph is represented as an adjacency list where graph[i] is a list of tuples (j, w), representing an edge from node i to node j with weight w. Your task is to find the longest path in the graph starting from any node.

    Function Signature:

    python

def longest_path(graph: list) -> int:

Parameters:

    graph (list): A list of lists, where graph[i] contains tuples (j, w) representing an edge from node i to node j with weight w.

Returns:

    int: The length of the longest path in the graph.

Example
    Input:
    graph = [
        [(1, 3), (2, 2)],
        [(3, 4)],
        [(3, 1)],
        []
    ]
    Output:
    7

Explanation:
The longest path is from node 0 -> node 1 -> node 3 with a total weight of 3 + 4 = 7.
