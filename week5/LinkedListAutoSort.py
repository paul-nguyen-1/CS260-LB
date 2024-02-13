class Node:
    def __init__(self, value):
        """ Initialize node value and next node value """
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """ Initialize head of linked list """
        self.head = None

    def insert(self, value):
        """
        Insertion of node value into linked list in auto sorted order
        value: Node
        """
        new_node = Node(value) # initialie node
        if not self.head or value < self.head.value: # If the list is empty or the new node has a smaller value than the head,
            new_node.next = self.head # reassign head value
            self.head = new_node # insert the new node at the beginning
            return

        current = self.head

        while current.next and current.next.value < value: # Traverse the list to find the correct position for the new node
            current = current.next

        # Insert the new node at the correct position
        new_node.next = current.next
        current.next = new_node
        
    def search(self, value) -> int:
        """Search for a value in the linked list.
        value: Node
        """
        current = self.head
        index = 0

        # Traverse the list to find the specified value and return its index
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return 
    
    def remove(self, value):
        """
        Deletion of node value in linked list
        value: Node
        """
        current = self.head

        # If the head contains the value, update the head to the next node
        if current and current.value == value:
            self.head = current.next
            return

        # Traverse the list to find and remove the node with the specified value
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        """ Display linked list inside of an array """
        current = self.head
        result = [] # We could use a string and concatenate, but we will use an array for this instead :)
        while current:
            result.append(current.value)
            current = current.next
        return result
