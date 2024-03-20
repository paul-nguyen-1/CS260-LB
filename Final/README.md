# Graph Design for Location Navigation

## Functions used in Graph
- Add Vertex: Create a new vertex object with the given name. If the graph is empty, set the new vertex as the head vertex -- otherwise, traverse the list of vertices and append the new vertex to the end.
- Add Edge: Retrieve the source and destination vertex objects from the graph. Create a new edge object with the destination vertex and distance. If the source vertex has no edges, set the new edge as the head edge. Otherwise, traverse the list of edges of the source vertex and append the new edge to the end.
- Get Vertex: Traverse the list of vertices in the graph. Compare the name or identifier of each vertex with the input. Return the vertex object if found, or return None if not found.
- Shortest Path: Initialize distances for all vertices to infinity and mark all vertices as unvisited. Set the distance of the source vertex to 0. Iterate through unvisited vertices to find the vertex with the minimum distance and mark it as visited to update the distances of its adjacent vertices. Return the distance of the destination vertex.
- Minimum Span Tree: Start from any vertex as the root. Traverse the graph, adding edges to the MST.

# Values Used in Vertex
- Name: Identifier for the vertex.
- Edges Head: Pointer to the first edge connected to this vertex.
- Next: Pointer to the next vertex in the graph.

# Values Used in Edge
- Destination Vertex: Pointer to the vertex at the end of the edge.
- Distance: Value representing the distance of the edge.
- Next: Pointer to the next edge connected to the same source vertex.

# Values Used in Graph
- Vertices Head: Pointer to the first vertex in the graph.
- Vertices: List of all vertices in the graph, allowing for efficient traversal and access.

# Implementation Complexities

## Add Vertex
- Best Case: O(1)
    - In the best case, adding a vertex involves simply setting it as the head vertex, which can be done in constant time.

- Worst Case: O(n)
    - In the worst case, adding a vertex requires traversing the list of vertices to find the end and append the new vertex.

## Add Edge
- Best Case: O(1)
    - In the best case, adding an edge involves simply appending it to the list of edges of the source vertex, which can be done in constant time.

- Worst Case: O(n)
    - In the worst case, adding an edge requires traversing the list of vertices to find the source and destination vertices.

## Shortest Path
- Best Case: O(n^2)
    - The best case occurs when the shortest path algorithm requires iterating through all vertices and their edges once to update distances.

- Worst Case: O(n^2)
    - The worst case occurs when the shortest path algorithm requires iterating through all vertices and their edges multiple times until no further updates are possible.

## Minimum Spanning Tree
- Best Case: O(n^2)
    - The best case occurs when the minimum spanning tree algorithm requires iterating through all vertices and their edges once to generate the minimum spanning tree.

- Worst Case: O(n^2)
    - The worst case occurs when the minimum spanning tree algorithm requires iterating through all vertices and their edges multiple times until the minimum spanning tree is complete.


## Test Implementation

#### Test Setup
- Initialize an instance of the Graph class
- Add vertices representing different locations: "New York", "Los Angeles", "Chicago", "Houston", and "San Francisco"
- Add edges between these vertices to simulate connections between the locations, specifying distances for each edge

#### Test Shortest Path
- Test the shortest_path method to find the shortest path between different pairs of locations
  - Test case 1: Find the shortest path between "New York" and "San Francisco"
    - Assert that the shortest path distance is 3400 miles (New York -> Los Angeles -> San Francisco)
  - Test case 2: Find the shortest path between "New York" and "Houston"
    - Assert that the shortest path distance is 1800 miles (New York -> Chicago -> Houston)

#### Test Minimum Spanning Tree
- Test the min_span_tree method to find the minimum spanning tree of the graph.
  - Create a list of expected edges in the minimum spanning tree, representing connections between all locations
  - Assert that all expected edges are present in the minimum spanning tree
