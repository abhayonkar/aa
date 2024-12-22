def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Initialize the set of visited nodes
    visited = set()

    # Initialize the set of unvisited nodes
    unvisited = set(graph)

    while unvisited:
        # Find the unvisited node with the smallest distance
        current_node = None
        for node in unvisited:
            if current_node is None or distances[node] < distances[current_node]:
                current_node = node

        # If the smallest distance is infinity, we can break
        if distances[current_node] == float('inf'):
            break

        # Update the distances to the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            if neighbor in unvisited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        # Mark the current node as visited
        visited.add(current_node)
        unvisited.remove(current_node)

    return distances

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'C'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from node {start_node}: {shortest_paths}")
