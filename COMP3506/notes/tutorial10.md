# Week 10 tutorial

#### Last 4 algorithms you can do in a graph

### Shortest path algorithms
- Each edge has a numerical weight
-  Weight can be: Cost, Distance, etc

Properties: 
1. **Subpath of a shortest path is itself a shortest path**
2. There is a tree of shortest paths from a start vertex to all other vertices

![Alt text](assets\IMG131.PNG)

### Dijkstra's algorithm
- Computes the shortest path from one vertex to all other vertices
- Greedy algorithm: At each step we relax the “vertices cloud”
- Edge relaxation
- Run time: O((n + m) log n)

Assumptions: 
- Graph is connected
- Edge weights are not negative


### Method:
Start at a vertex, with all unexplored vertices as weight ∞.
1. For all unvisited vertices that you have a direct path to, update the 
weights if they are smaller than the current weight. 
2. Visit a previously unvisited vertex that takes the least “cost”/“effort”
● Keep track of the edges you have travelled along
Repeat this until all vertices have been visited.

![Alt text](assets\IMG132.PNG)

![Alt text](assets\IMG133.PNG)


### DAG - based algorithm Example

![Alt text](assets\IMG134.PNG)

### Minimum spanning tree

- Spanning Subgraph: Subgraph of G contain all vertices
- Tree
  - Connected acyclic graph
Spanning Tree
  - Subset of edges of graph G that form a tree & hit all vertices of G
- Minimum Spanning Tree
  - Spanning tree of a weighted graph with minimum total edge weight

**Cycle Property**
- Cycle Property
  - MST should have no cycles
- Partition Property:
  - Partition G’s vertices into subsets 
U & V 
- Let e be an edge of minimum 
weight across the partition
- There is a minimum spanning 
tree of G containing edge e

![Alt text](assets\IMG135.PNG)

### Prim-Jarnik’s Algorithm

- Purpose: Find MST
- Greedy algorithm
- Run time: O((n + m) log (n))
1. First edge: Find the smallest weighted edge
2. Until you create a MST:
  - Find the next minimum weighted edge that is already connected to the current tree. Ensure the edge you select does not produce a cycle (violates the concept of the tree)

|before| after|
|---|---|
![Alt text](assets\IMG136.PNG) | ![Alt text](assets\IMG137.PNG)


### Kruskal's algorithm

- Purpose: Find MST
- Greedy algorithm
- Run time: O((n + m) log n)
1. Select smallest edge anywhere in the graph
- Discard the edge if it forms a cycle