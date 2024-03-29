import unittest
from ArrayListAutoSort import ArrayList

class TestArrayListMethods(unittest.TestCase):

    def setUp(self):
        """ Initialize array list"""
        self.array_list = ArrayList()

    def test_insert(self):
        """ Test insertion to array list """
        
        # Test inserting 5 into array list
        self.array_list.insert(5)
        self.assertEqual(self.array_list.array_list, [5])

        # Test inserting less than 5 into array list
        self.array_list.insert(3)
        self.assertEqual(self.array_list.array_list, [3, 5])

        # Test inserting greater than 3 and 5 into array list
        self.array_list.insert(8)
        self.assertEqual(self.array_list.array_list, [3, 5, 8])
        
        # Test inserting least value amount into array list
        self.array_list.insert(1)
        self.assertEqual(self.array_list.array_list, [1, 3, 5, 8])
        
        # Test inserting number already in linkedlist
        self.array_list.insert(5)
        self.assertEqual(self.array_list.array_list, [1, 3, 5, 5, 8])
        
         # Test inserting upper boundary into array list
        self.array_list.insert(14)
        self.assertEqual(self.array_list.array_list, [1, 3, 5, 5, 8, 14])

    def test_remove(self):
        self.array_list.array_list = [1, 3, 5, 8]

        # Remove 5 from array
        self.array_list.remove(5)
        self.assertEqual(self.array_list.array_list, [1, 3, 8])

        # Remove 1 from array
        self.array_list.remove(1)
        self.assertEqual(self.array_list.array_list, [3, 8])

        # Remove non existant value
        self.array_list.remove(10)
        self.assertEqual(self.array_list.array_list, [3, 8])
        
        # Remove greatest value
        self.array_list.remove(8)
        self.assertEqual(self.array_list.array_list, [3])
        
    def test_search(self):
        self.array_list.array_list = [1, 2, 7, 11]
        
        # Check for the first value
        self.assertEqual(self.array_list.search(1), 0)
        
        # Check for the last value
        self.assertEqual(self.array_list.search(11), 3)
        
        # Check for the 3rd value
        self.assertEqual(self.array_list.search(7), 2)
        
        # Check for the second value
        self.assertEqual(self.array_list.search(2), 1)
        

if __name__ == '__main__':
    unittest.main()


