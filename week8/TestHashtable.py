import unittest

from Hashtable import Hashtable

class TestHashtable(unittest.TestCase):
    def setUp(self):
        self.hashtable = Hashtable(10)

    def test_insert_and_contains(self):
        self.hashtable.insert(1, 10)
        self.assertEqual(self.hashtable.contains(1), 10)

        # Inserting the same key should update the value
        self.hashtable.insert(1, 20)
        self.assertEqual(self.hashtable.contains(1), 20)

        # Inserting a new key
        self.hashtable.insert(2, 30)
        self.assertEqual(self.hashtable.contains(2), 30)

    def test_delete(self):
        self.hashtable.insert(1, 10)
        self.hashtable.insert(2, 20)

        # Deleting an existing key
        self.hashtable.delete(1)
        self.assertEqual(self.hashtable.contains(1), 'not found')

        # Deleting a non-existing key should have no effect
        self.hashtable.delete(3)
        self.assertEqual(self.hashtable.contains(2), 20)

    def test_collision_handling(self):
        # Simulate a collision by setting the size to 1
        self.hashtable.size = 1
        self.hashtable.insert(1, 10)
        self.hashtable.insert(11, 20)  # This should trigger a collision

        # Both keys should be in the hashtable
        self.assertEqual(self.hashtable.contains(1), 10)
        self.assertEqual(self.hashtable.contains(11), 20)

    def test_not_found_case(self):
        self.assertEqual(self.hashtable.contains(1), 'not found')

if __name__ == '__main__':
    unittest.main()
