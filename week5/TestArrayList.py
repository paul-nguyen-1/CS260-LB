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
        
        # Test inserting between 5 and 8 into array list
        self.array_list.insert(7)
        self.assertEqual(self.array_list.array_list, [1, 3, 5, 7, 8])
        
         # Test inserting upper boundary into array list
        self.array_list.insert(14)
        self.assertEqual(self.array_list.array_list, [1, 3, 5, 7, 8, 14])

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

if __name__ == '__main__':
    unittest.main()


