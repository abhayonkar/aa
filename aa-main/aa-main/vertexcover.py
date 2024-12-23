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






















# ### **Vertex Cover Problem**

# #### **Aim**  
# To find the minimum vertex cover in a graph, i.e., the smallest set of vertices such that each edge in the graph has at least one endpoint in the set.

# ---

# #### **Working**  
# The **vertex cover** problem is NP-complete, meaning there is no known polynomial-time solution for it in the general case. However, we can approximate the problem using a greedy algorithm.

# 1. **Greedy Approach**:  
#    - Select an edge that is not yet covered by the current set of vertices.
#    - Add both endpoints of that edge to the vertex cover.
#    - Remove all edges incident to those two vertices.
#    - Repeat until all edges are covered.

# This approach guarantees a **2-approximation**, meaning the size of the vertex cover found will be at most twice the size of the minimum vertex cover.

# ---

# #### **Pseudo Code**  
# ```  
# Algorithm: Greedy Vertex Cover  
# Input: Graph G with vertices V and edges E  
# Output: A vertex cover set C

# 1. Initialize C = ∅ (empty set)
# 2. while there are uncovered edges in E do  
# 3.     Select an uncovered edge (u, v)  
# 4.     Add u and v to C  
# 5.     Remove all edges incident to u and v from E  
# 6. Return C  
# ```

# ---

# #### **Complexity and Recurrence Formula**  
# - **Time Complexity**:  
#   - \(O(V + E)\) where \(V\) is the number of vertices and \(E\) is the number of edges.  
#   - This is because we iterate over edges and vertices, removing them once they are covered.

# - **Space Complexity**:  
#   - \(O(V + E)\) due to storing the graph and the vertex cover set.

# ---

# #### **Conclusion**  
# The **Vertex Cover Problem** is NP-complete in its general form. However, the greedy algorithm provides a good approximation with a 2-factor approximation guarantee. The algorithm is efficient and works well for many practical scenarios, though it is not always optimal.

# ### **Explanation**:
# 1. The graph is represented as an adjacency list.
# 2. We start with an empty set `cover`.
# 3. We iterate through the edges of the graph, adding both endpoints of each edge to the cover, and then remove all edges incident to those vertices.
# 4. The algorithm continues until all edges are covered.

