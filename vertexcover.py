def vertex_cover(graph):
    vertex_cover_set = set()
    edges = {(u, v) for u in graph for v in graph[u]}

    while edges:
        # Find the vertex with the maximum number of uncovered edges
        max_vertex = max(graph.keys(), key=lambda v: sum(1 for u in graph[v] if (v, u) in edges or (u, v) in edges))
        vertex_cover_set.add(max_vertex)

        # Mark all edges incident to the selected vertex as covered
        edges_to_remove = {(v, u) for v, u in edges if v == max_vertex or u == max_vertex}
        edges -= edges_to_remove

    return vertex_cover_set

# Example usage
graph = {
    1: [2, 3, 4],
    2: [1, 3, 5],
    3: [1, 2, 4, 5],
    4: [1, 3]
}

vc = vertex_cover(graph)
print("Vertex Cover Set:", vc)
