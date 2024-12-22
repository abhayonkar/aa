def topological_sort(graph, in_degree):
    zero_in_degree = [node for node in range(len(graph)) if in_degree[node] == 0]
    topo_order = []

    while zero_in_degree:
        node = zero_in_degree.pop(0)
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    if len(topo_order) == len(graph):
        return topo_order
    else:
        return []  # Graph has a cycle

def longest_path_in_dag(graph):
    n = len(graph)
    in_degree = [0] * n

    for node in range(n):
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    topo_order = topological_sort(graph, in_degree)

    if not topo_order:
        return "Graph has a cycle"

    dist = [-float('inf')] * n
    dist[topo_order[0]] = 0

    for node in topo_order:
        for neighbor in graph[node]:
            if dist[neighbor] < dist[node] + 1:
                dist[neighbor] = dist[node] + 1

    max_dist = max(dist)
    return max_dist

# Example usage:
graph = [
    [1, 2],  # Node 0 has edges to nodes 1 and 2
    [3],     # Node 1 has an edge to node 3
    [3],     # Node 2 has an edge to node 3
    []       # Node 3 has no outgoing edges
]

print("Longest path in the DAG:", longest_path_in_dag(graph))
