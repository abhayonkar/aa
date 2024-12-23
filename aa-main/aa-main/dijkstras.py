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






















# ### **7. Dijkstra’s Algorithm**

# #### **Aim**  
# To find the shortest path from a source vertex to all other vertices in a graph with non-negative weights.

# #### **Working**  
# The algorithm uses a priority queue to iteratively select the vertex with the smallest distance and update distances to its neighbors.

# #### **Pseudo Code**  
# ```  
# Algorithm: Dijkstra  
# Input: Graph G, source vertex s  
# Output: Shortest path from s to all vertices  

# 1. Initialize dist[v] = ∞ for all vertices except dist[s] = 0  
# 2. Add all vertices to a priority queue Q  
# 3. while Q is not empty do  
# 4.     u = vertex in Q with min dist[u]  
# 5.     for each neighbor v of u do  
# 6.         if dist[u] + weight(u, v) < dist[v] then  
# 7.             dist[v] = dist[u] + weight(u, v)  
# 8. Return dist  
# ```

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**: \(O((V + E) \log V)\) using a min-heap  
# - **Space Complexity**: \(O(V)\)  
# - **Recurrence Relation**:  
#   \(T(V) = T(V-1) + O(\log V)\)

# #### **Conclusion**  
# Dijkstra's algorithm efficiently solves shortest path problems for graphs with non-negative weights.