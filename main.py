
### 2. `main.py`

"""python
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

from collections import deque

def longest_path(graph: list) -> int:
    n = len(graph)
    topo_order = topological_sort(graph)
    dp = [-float('inf')] * n
    
    for node in topo_order:
        if dp[node] == -float('inf'):
            dp[node] = 0
        for neighbor, weight in graph[node]:
            dp[neighbor] = max(dp[neighbor], dp[node] + weight)
    
    longest_path_length = max(dp)
    return longest_path_length

def topological_sort(graph):
    n = len(graph)
    in_degree = [0] * n
    for node in range(n):
        for neighbor, _ in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor, _ in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order

def calculate_longest_path(graph, topo_order):
    n = len(graph)
    dp = [-float('inf')] * n
    
    for node in topo_order:
        if dp[node] == -float('inf'):
            dp[node] = 0 
        for neighbor, weight in graph[node]:
            dp[neighbor] = max(dp[neighbor], dp[node] + weight)
    
    longest_path_length = max(dp)
    return longest_path_length

