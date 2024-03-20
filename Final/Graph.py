class Vertex:
    def __init__(self, name):
        self.name = name  # Name of the vertex
        self.edges_head = None  # Head of the linked list of edges connected to this vertex
        self.next = None  # Pointer to the next vertex in the graph

class Edge:
    def __init__(self, destination_vertex, distance=0):
        self.destination_vertex = destination_vertex  # Destination vertex of the edge
        self.distance = distance  # Distance attribute representing the distance in miles
        self.next = None  # Pointer to the next edge in the linked list

class Graph:
    def __init__(self):
        self.vertices_head = None  # Head of the linked list of vertices
        self.vertices = []  # List to keep track of all vertices in the graph

    def add_vertex(self, vertex_name):
            """
        Add a new vertex to the graph

        Value:
            - vertex_name: string
        """
            # Initialize new vertex to be added in graph
            new_vertex = Vertex(vertex_name)
            if not self.vertices_head:
                self.vertices_head = new_vertex
            else:
                current = self.vertices_head
                # Iterate through linked list
                while current.next:
                    current = current.next
                current.next = new_vertex # Append new_vertex to the end of the linked list
            self.vertices.append(new_vertex) # Add new vertex to the list of vertices

    def add_edge(self, source, destination_vertex, distance=0):
        """
        Add a new edge between two vertices in the graph.

        Values:
            - source: string
            - destination_vertex: string
            - distance: int
        """
        source_vertex = self.get_vertex(source) # Retrieve the source vertex object from its name
        if source_vertex:
            destination_vertex_obj = self.get_vertex(destination_vertex) # Retrieve the destination vertex object from its name
            if destination_vertex_obj:
                new_edge = Edge(destination_vertex_obj, distance) # Create a new edge with the destination vertex and distance
                if not source_vertex.edges_head: # Check if the source vertex has no existing edges
                    source_vertex.edges_head = new_edge # Set new edge as first edge, if no existing edges
                else:
                     # Traverse the linked list of edges to find the last edge
                    current = source_vertex.edges_head
                    while current.next:
                        current = current.next
                    current.next = new_edge # Assign the new edge to the end of the linked list
            else:
                print(f"Destination vertex '{destination_vertex}' does not exist.") # Check if destination vertex doesn't exist
        else:
            print(f"Source vertex '{source}' does not exist.") # Check if source vertex doesn't exist


    def get_vertex(self, name):
        """
        Get the vertex with the given name

        Value: 
            - name: string

        Returns: The vertex with the given name, or None if not found
        """
        current = self.vertices_head # Search from the head of the vertices linked list
        while current:
            if current.name == name: # Check if the current vertex's name matches the given name
                return current # Return the current vertex if found
            current = current.next # Move to the next vertex in the linked list
        return None # Return None if the vertex with the given name is not found

    def shortest_path(self, source, destination):
        """
        Find the shortest path between two vertices in the graph

        Values:
            source: string
            destination: string

        Returns: The shortest path distance between the source and destination vertices, or None if either vertex is not found
        """
        # Initialize distances for all vertices
        current_vertex = self.vertices_head
        while current_vertex:
            current_vertex.distance = float('inf')  # Set distance of each vertex to infinity
            current_vertex.visited = False  # Mark each vertex as not visited
            current_vertex = current_vertex.next  # Move to the next vertex in the linked list

        # Find the source vertex
        source_vertex = self.get_vertex(source)
        if source_vertex is None:
            return None  # Return None if source vertex not found

        source_vertex.distance = 0 # Set distance of source vertex to 0

        # Main loop to find shortest path
        while True:  # Infinite loop to continuously find the vertex with the minimum distance
            # Find the vertex with the minimum distance among unvisited vertices
            min_distance = float('inf')  # Initialize the minimum distance 
            min_vertex = None  # Initialize the vertex with the minimum distance 
            current_vertex = self.vertices_head  # Start from the head of the vertices linked list
            
            while current_vertex:  # Iterate through each vertex in the graph
                if not current_vertex.visited and current_vertex.distance < min_distance: # Check if the current vertex has not been visited and has a smaller distance than the current minimum distance
                    min_distance = current_vertex.distance  # Update the minimum distance
                    min_vertex = current_vertex  # Update the vertex with the minimum distance
                current_vertex = current_vertex.next  # Move to the next vertex in the linked list of vertices

            # Break the loop if all vertices are visited or if min_vertex is None
            if min_vertex is None:
                break

            min_vertex.visited = True # Mark min_vertex as visited

            # Update distances of adjacent vertices
            current_edge = min_vertex.edges_head # Start from the first edge of the current vertex
            while current_edge: # Iterate through each edge of the current vertex
                neighbor_vertex = current_edge.destination_vertex # Get the vertex connected by the current edg
                if not neighbor_vertex.visited: # Check if the neighbor vertex has not been visited
                    distance_through_min_vertex = min_vertex.distance + current_edge.distance # Calculate the distance through the current vertex to the neighbor vertex
                    # Update the distance of the neighbor vertex if the calculated distance is shorter
                    if distance_through_min_vertex < neighbor_vertex.distance:
                        neighbor_vertex.distance = distance_through_min_vertex # Update the distance of the neighbor vertex
                current_edge = current_edge.next # Move to the next edge in the linked list of edges

        destination_vertex = self.get_vertex(destination) # Retrieve the destination vertex
        
        # Check if the destination vertex is not found
        if destination_vertex is None:
            print("Destination vertex not found.")

        # Check if the distance of the destination vertex is not infinity
        if destination_vertex.distance != float('inf'):
            return destination_vertex.distance


    def min_span_tree(self):
        """
        Find the minimum spanning tree of the graph

        Returns: List representing edges in the minimum spanning tree, or None if graph is empty
        """
        min_span_tree = []  # Initialize an empty list to store the minimum spanning tree edges
        start_vertex = self.vertices_head  # Start from the head of the vertices linked list
        if not start_vertex:  # Check if the graph is empty
            return None  # Return an empty list if the graph is empty
        
        while start_vertex:  # Iterate through each vertex in the graph
            edge = start_vertex.edges_head  # Get the first edge of the current vertex
            while edge:  # Iterate through each edge of the current vertex
                min_span_tree.append((start_vertex.name, edge.destination_vertex.name)) # Append edge to the minimum spanning tree list
                edge = edge.next  # Move to the next edge in the linked list of edges
            start_vertex = start_vertex.next  # Move to the next vertex in the linked list of vertices
        return min_span_tree  # Return the list representing edges in the minimum spanning tree

