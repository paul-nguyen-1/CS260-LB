import unittest
from Graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        
        # Test adding vertex
        self.graph.add_vertex("New York")
        self.graph.add_vertex("Los Angeles")
        self.graph.add_vertex("Chicago")
        self.graph.add_vertex("Houston")
        self.graph.add_vertex("San Francisco")
        
        # Test adding edges
        self.graph.add_edge("New York", "Los Angeles", 3000)  # Distance: 3000 miles
        self.graph.add_edge("New York", "Chicago", 800)      # Distance: 800 miles
        self.graph.add_edge("Los Angeles", "Chicago", 2000)  # Distance: 2000 miles
        self.graph.add_edge("Los Angeles", "Houston", 1500)  # Distance: 1500 miles
        self.graph.add_edge("Chicago", "Houston", 1000)      # Distance: 1000 miles
        self.graph.add_edge("Los Angeles", "San Francisco", 400)  # Distance: 400 miles
        self.graph.add_edge("Houston", "San Francisco", 1800)     # Distance: 1800 miles

    def test_shortest_path(self):
        shortest_path = self.graph.shortest_path("New York", "San Francisco") # Test shortest path between New York and San Francisco
        self.assertEqual(shortest_path, 3400) # Expected shortest path distance: 3400 miles (New York 3000 -> LA  400 -> San Francisco)
        
        shortest_path = self.graph.shortest_path("New York", "Houston") # Test shortest path between New York and Houston
        self.assertEqual(shortest_path, 1800) # Expected shortest path distance: 1800 miles (New York 800 --> Chicago 1000 --> Houston)

    def test_min_span_tree(self):
        expected_edges = [
            ("New York", "Los Angeles"),
            ("New York", "Chicago"),
            ("Los Angeles", "San Francisco"),
            ("Los Angeles", "Chicago"),
            ("Los Angeles", "Houston"),
            ("Chicago", "Houston"),
            ("Houston", "San Francisco")
        ] # All expected edges in tree, representing connections between all locations
        
        min_span_tree = self.graph.min_span_tree()
        
        # Check all expected edge present in the minimum spanning tree
        for edge in expected_edges:
            self.assertIn(edge, min_span_tree)

if __name__ == '__main__':
    unittest.main()
