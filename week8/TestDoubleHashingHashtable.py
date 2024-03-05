import unittest
from Hashtable import DoubleHashingHashtable

class TestDoubleHashingHashtable(unittest.TestCase):
    def setUp(self):
        self.double_hashtable = DoubleHashingHashtable(10)

    def test_insert_and_contains(self):
        self.double_hashtable.insert(1, 10)
        self.assertEqual(self.double_hashtable.contains(1), 10)

        # Inserting the same key should update the value
        self.double_hashtable.insert(1, 20)
        self.assertEqual(self.double_hashtable.contains(1), 20)

        # Inserting a new key
        self.double_hashtable.insert(2, 30)
        self.assertEqual(self.double_hashtable.contains(2), 30)

    def test_delete(self):
        self.double_hashtable.insert(1, 10)
        self.double_hashtable.insert(2, 20)

        # Deleting an existing key
        self.double_hashtable.delete(1, 7)  # Pass a prime number for the secondary hash
        self.assertEqual(self.double_hashtable.contains(1), 'not found')

        # Deleting a non-existing key should have no effect
        self.double_hashtable.delete(3, 7)  # Pass a prime number for the secondary hash
        self.assertEqual(self.double_hashtable.contains(2), 20)

    def test_collision_handling(self):
        # Simulate a collision by setting the size to 1
        self.double_hashtable.size = 1
        self.double_hashtable.insert(1, 10)
        self.double_hashtable.insert(11, 20)  # This should trigger a collision

        # Both keys should be in the hashtable
        self.assertEqual(self.double_hashtable.contains(1), 10)
        self.assertEqual(self.double_hashtable.contains(11), 20)

    def test_not_found_case(self):
        self.assertEqual(self.double_hashtable.contains(1), 'not found')

if __name__ == '__main__':
    unittest.main()
