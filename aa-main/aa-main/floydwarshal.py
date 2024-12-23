def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(n):
        if dist[i][i] < 0:
            return "Graph contains a negative cycle"

    return dist

# Example usage
graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

result = floyd_warshall(graph)

print(result)






















### **3. Floyd-Warshall Algorithm**

# #### **Aim**  
# To compute shortest paths between all pairs of vertices in a weighted graph.

# #### **Working**  
# The algorithm iteratively updates the shortest path between all pairs of vertices using a dynamic programming approach, checking if paths through an intermediate vertex yield a shorter route.

# #### **Pseudo Code**  
# ```  
# Algorithm: Floyd-Warshall  
# Input: Graph G with vertices V and weights W  
# Output: All-pairs shortest path distances  

# 1. Initialize dist[i][j] = W[i][j] for all edges, ∞ for no direct edge  
# 2. for k = 1 to |V| do  
# 3.     for i = 1 to |V| do  
# 4.         for j = 1 to |V| do  
# 5.             dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  
# 6. Return dist  
# ```

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**: \(O(V^3)\)  
# - **Space Complexity**: \(O(V^2)\)  
# - **Recurrence Relation**:  
#   \(dist[i][j] = \min(dist[i][j], dist[i][k] + dist[k][j])\)

# #### **Conclusion**  
# Floyd-Warshall is a simple and effective algorithm for dense graphs but is inefficient for sparse graphs due to its cubic time complexity.