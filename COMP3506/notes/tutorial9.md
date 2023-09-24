# Tutorial 9

### Graph basics
- **Edges** the paths that connect nodes
  - Undirected: unordered pair of vertices
- **Vertices** nodes
  - Store information, such as city, place, etc.
- Undirected graph:: all edges are undirected
- Directed graph: all edges are directed

### Terminology: vertices
- **End vertices** Endpoints of an edge
  - U & V are end vertices of a
- **Edge incident of a vertex**
- a, d, b, are incident on V

- **Degree of a vertex**
  - #' of edges coming off a vertex
- **Parallel edges**
  - 2 edges with the same end vertices
  - h and i are parallel edges
- **self-loop**
  - Edge that connect the vertex to itself
  - j is a self-loop

![Alt text](assets\image-4.png)


### Paths
- Alternativ sequence of vertices and edges
- Starts and ends with a vertex
- Each edge is preceded and followed by its endpoints
- **Simple path**
  - All vertices and adges are distinct ``P1``

![Alt text](assets\image-5.png)

### Cycle
- Have to start and end at the same vertex
- **Simple cycle**
  -  Cycle where all vertices are distinct, 
(except the first and last)
  - All edges are distinct

### Subgraph
- subset of vertixes and edges
  
**Spanning subgraph**
-  S has all of G’s vertices

### Connected graph
- simple path between every pair of vertices
-  **Connected component**

### Trees and forests
**Free (unrooted) tree**
-  Undirected graph the is connected & 
has no simple cycles

**Forest**
- Multiple free unrooted trees

![Alt text](assets\image-6.png)

### Spanning trees and forests
**Spanning Tree**
- Spanning subgraph that is a tree
  
**Spanning Forest**
- Spanning subgraph that is a forest

![Alt text](assets\image-7.png)

### Properties
- $\sum_{v} deg(v) = 2m$ - the total degree of vertices is twicethe number of edges (duh)
- In an undirected graph with no self-loops and no multiple edges
  - $m \le n(n-1) \div 2$

### Density
- Undirected simple graph
  - $𝐷 = \dfrac{2𝑚}{𝑛(𝑛−1)}$
- Directed simple graph
  - $𝐷 = \dfrac{m}{𝑛(𝑛−1)}$
- Maximum density is 1
- Minimum density is 0
- Sparse
  - $m  ≅ O(n)$  
- Dense
  - $m  ≅ O(n^{2})$

### Edge list
- Sequence of edges represented by 
vertex pairs
- Can be represented as a matrix
  - Two-column if there are no edge 
weights
  - Three-column, otherwise

- List stores each vertex
  - For each vertex, it stores connected edges 

### Adjacency map structure
List stores each vertex
-  For each vertex, it stores a hash map
  - Key: vertex it can reach
  - Value: Edge to traverse to reach vertex

![Alt text](assets\image-8.png)

### Adjacency matrix structure
- 2D array
- Rows & columns are vertices
- Cells, if the value is stored, is an edge that 
connects the vertices

![Alt text](assets\image-9.png)

### Performance

![Alt text](assets\image-10.png)

### Depth first search
-  Run Time: O(n + m)
-  n is # of edges, m is # of vertices

### Depth first search: Algorithm
Start at a vertex, add it to the stack and mark it as explored
1. Remove vertex V from the stack
2. Traverse to vertex W along an unexplored edge that is connected to 
vertex V.
  - If W is explored: Mark as Back edge. Step 2
  - If W is unexplored: Mark as Discovery Edge. Step 3.
1. Push V to the stack. Go to step 2 using vertex W.
2. Repeat Steps 2 & 3 until there are no unexplored edges. Go to Step 1.
Repeat until the stack is empty

### Breadth-first search
- Run Time: O(n + m)
- Keep track of: 
  - Unexplored Edge, Discovery Edge & Cross Edge
  - Unexplored Vertex & Visited Vertex
- Use a queue
- Good for: Compute a spanning forest, find a simple cycle, find the 
shortest path

#### Process:
  - Add starting vertex to the queue and mark it as visited
1. Remove vertex V from the queue, visit all vertices connected to V.
  - For all unexplored vertices visited: add them to the queue and mark 
them as visited
1. Mark edge as:
  - Discovery Edge if leads to an unexplored vertex
  - Cross Edge if leads to an explored vertex
1. Repeat steps 1 & 2 until the queue is empty

### Digraphs
- all edges are directed
- Adapted DFS to Directed DFS.

#### Reachability
- From vertex V, what other vertices can be reached?

### Strong connectivity
Each vertex can reach all other vertices
- To determine if Strong Connectivity:
  - Pick a vertex v in G
  - Perform a DFS from v in G
    - if there’s a w not visited, false
  - Let G’ be G with edges reversed
  - Perform a DFS from v in G’
    - if there’s a w not visited, false
    - else, true

### Strongly connected Component
Subgraph where each vertex can 
reach all other vertices

![Alt text](assets\image-11.png)

### Transitive Closure
- Add more edges based on transitive closure
- For a Digraph G, we can create G*
  - G* has the same vertices as G
  - If there is a directed path 
between 2 vertices, we add 
directed edge between these 
vertices
- Use Floyd-Warshall Algorithm to find 
G*

![Alt text](assets\image-12.png)

### Topological orger and Directed Acyclic Graphs
- Ordering of nodes in a directed graph where for each node in a path 
from node A to node B, node A appears before node B. 
- Order is not unique
- Not all graphs have a topological order (graphs with cycles)
- Only Directed Acyclic Graphs (DAG) have a topological order

| Graph before | Graph after
|---|---
| ![Alt text](assets\image-13.png) | ![Alt text](assets\image-14.png)
