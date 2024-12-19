# Kruskal's Algorithm for Minimum Spanning Tree (MST)

## a. Algorithms to Find MST using Kruskal’s Algorithm

### Step-by-Step Algorithm

Kruskal’s algorithm is used to find the Minimum Spanning Tree (MST) of a connected, undirected graph. The MST connects all the vertices together using the minimum possible edge weights, and no cycles are formed.

#### Algorithm Steps:

1. **Sort all edges** in non-decreasing order based on their weights.
2. **Initialize the Union-Find (Disjoint-Set)** data structure:
   - This structure helps track and merge sets of connected components in the graph.
3. **Iterate through the sorted edges**:
   - For each edge `(u, v, weight)`, check if the vertices `u` and `v` are in the same connected component by using the **Find** operation.
   - If they belong to different components, add the edge to the MST and merge the two components using the **Union** operation.
4. **Stop when the MST contains `V-1` edges** (where `V` is the number of vertices in the graph).

### Union-Find Data Structure Operations:

- **Find Operation**: This operation determines the root of a vertex and uses **path compression** to speed up future operations.
- **Union Operation**: This operation merges two sets containing the vertices. It uses **union by rank** to keep the tree structure flat.

---

### Pseudo-code for Kruskal's Algorithm

```plaintext
Kruskal(G):
    Input: G = (V, E)  // A graph with V vertices and E edges
    Output: MST (Minimum Spanning Tree)

    1. Sort all edges in G by non-decreasing order of their weight.
    2. Initialize a Union-Find data structure for V vertices.
    3. Initialize an empty list MST to store the edges of the MST.
    4. For each edge (u, v) in sorted edge list:
        a. If Find(u) != Find(v):  // Check if u and v are in different sets
            i. Add edge (u, v) to MST.
            ii. Perform Union(u, v) to merge the sets containing u and v.
    5. Return the MST and its total weight.
b. Detailed Analysis of the Algorithm
Time Complexity Analysis
Sorting the Edges:

The first step is sorting all edges in non-decreasing order of their weight. Sorting a list of E edges takes O(E log E) time, where E is the number of edges in the graph.
Union-Find Operations:

Find Operation: This operation determines the root of a vertex and uses path compression to make future queries faster. The Find operation runs in O(α(V)) time, where α(V) is the inverse Ackermann function. The function grows very slowly, so it is nearly constant for practical purposes.
Union Operation: The Union operation merges two sets into one, using union by rank to maintain a balanced tree structure. This operation also runs in O(α(V)) time.
The total time complexity for performing the Find and Union operations for each edge is O(E α(V)), where E is the number of edges, and V is the number of vertices in the graph.
Overall Time Complexity:

Combining the time for sorting the edges and performing the union-find operations, the overall time complexity is:
𝑂(𝐸log𝐸+𝐸𝛼(𝑉))≈𝑂(𝐸log𝐸)

This is because α(V) grows extremely slowly, and for large graphs, O(E log E) will dominate.
