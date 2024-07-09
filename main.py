def longest_path(graph: list) -> int:
    def topological_sort(graph):
        n = len(graph)
        visited = [False] * n
        stack = []

        def dfs(node):
            visited[node] = True
            for neighbor, _ in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        stack.reverse()
        return stack

    def calculate_longest_path(graph, topo_order):
        n = len(graph)
        dist = [-float('inf')] * n
       
        has_incoming_edge = [False] * n
        for u in range(n):
            for v, _ in graph[u]:
                has_incoming_edge[v] = True
        
        for i in range(n):
            if not has_incoming_edge[i]:
                dist[i] = 0
        
        for node in topo_order:
            if dist[node] != -float('inf'):
                for neighbor, weight in graph[node]:
                    if dist[neighbor] < dist[node] + weight:
                        dist[neighbor] = dist[node] + weight
        
        return max(dist)

    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)