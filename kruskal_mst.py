class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Initially, each node is its own parent
        self.rank = [0] * n  # Used for union by rank

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    # edges is a list of tuples (weight, u, v), where u and v are vertices, and weight is the edge weight
    edges.sort()  # Sort edges by their weight

    uf = UnionFind(n)
    mst = []  # To store the edges of the MST
    mst_weight = 0  # To store the total weight of the MST

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):  # If u and v are in different sets, no cycle
            uf.union(u, v)
            mst.append((u, v, weight))  # Add this edge to MST
            mst_weight += weight  # Update the total weight

    return mst, mst_weight
