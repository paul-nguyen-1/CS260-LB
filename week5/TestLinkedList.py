import unittest
from LinkedListAutoSort import LinkedList

class TestLinkedListMethods(unittest.TestCase):

    def setUp(self):
        """ Initialize linkedlist"""
        self.linked_list = LinkedList()

    def test_insert(self):
        """ Test insertion for linked list """
        self.linked_list.insert(5)
        self.assertEqual(self.linked_list.display(), [5])
        
        # Add a number less than 5 into linked list 
        self.linked_list.insert(2)
        self.assertEqual(self.linked_list.display(), [2, 5])

        # Add a number greater than 2 and 5 into linked list
        self.linked_list.insert(8)
        self.assertEqual(self.linked_list.display(), [2, 5, 8])

        # Add a number greater than 2 but less than 5 into linked list
        self.linked_list.insert(4)
        self.assertEqual(self.linked_list.display(), [ 2, 4, 5, 8])
        
        # Add a number greater than 5 into linked list
        self.linked_list.insert(5)
        self.assertEqual(self.linked_list.display(), [ 2, 4, 5, 5, 8])
        

    def test_remove(self):
        """ Test removing from linked list """
        
        # Display linked list values inside array
        self.linked_list.insert(1)
        self.linked_list.insert(3)
        self.linked_list.insert(5)

        # Remove value 3 from linked list
        self.linked_list.remove(3)
        self.assertEqual(self.linked_list.display(), [1, 5])

        # Remove value 1 from linked list
        self.linked_list.remove(1)
        self.assertEqual(self.linked_list.display(), [5])

        # Remove a value that wasn't present in linked list
        self.linked_list.remove(10)
        self.assertEqual(self.linked_list.display(), [5])
        
        # Remove last value that was inside linked list
        self.linked_list.remove(5)
        self.assertEqual(self.linked_list.display(), [])
        
    def test_search(self):
        self.linked_list.insert(1)
        self.linked_list.insert(11)
        self.linked_list.insert(7)
        self.linked_list.insert(2)
        
        # Check for the first value
        self.assertEqual(self.linked_list.search(1), 0)
        
        # Check for the last value
        self.assertEqual(self.linked_list.search(11), 3)
        
        # Check for the 3rd value
        self.assertEqual(self.linked_list.search(7), 2)
        
        # Check for the second value
        self.assertEqual(self.linked_list.search(2), 1)

if __name__ == '__main__':
    unittest.main()
