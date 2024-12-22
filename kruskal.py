class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(edges, num_vertices):
    result = []
    edges = sorted(edges, key=lambda edge: edge.weight)

    parent = []
    rank = []

    for node in range(num_vertices):
        parent.append(node)
        rank.append(0)

    i = 0
    e = 0

    while e < num_vertices - 1:
        src, dest, weight = edges[i].src, edges[i].dest, edges[i].weight
        i += 1
        x = find(parent, src)
        y = find(parent, dest)

        if x != y:
            e += 1
            result.append(edges[i-1])
            union(parent, rank, x, y)

    return result

# Example usage
edges = [
    Edge(0, 1, 10),
    Edge(0, 2, 6),
    Edge(0, 3, 5),
    Edge(1, 3, 15),
    Edge(2, 3, 4)
]

num_vertices = 4
mst = kruskal(edges, num_vertices)

print("Edges in the constructed MST")
for edge in mst:
    print(f"{edge.src} -- {edge.dest} == {edge.weight}")
