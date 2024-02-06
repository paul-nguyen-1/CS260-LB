class Node:
    """Represents a node in a linked list"""

    def __init__(self, value):
        """ Initializes value and next members """
        self.value = value  # Node value of Linked List
        self.next = None  # Next node value on Linked List

    def get_next(self):
        """ Get next node """
        return self.next # get next node in linked list

    def set_next(self, updated_node):
        """ Set next node """
        self.next = updated_node # update next node with updated node


class LinkedList:
    """A linked list implementation of the List"""

    def __init__(self):
        """ Initializes head """
        self.head = None # Top value of LinkedList

    def add(self, val):
        """ Method to add a node containing val to the end of the linked list"""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node # assign new node to head val if there is nothing in linked list
        else:
            current = self.head # initialize current pointer to head of linked list
            while current.get_next() is not None:
                current = current.get_next() # keep traversing linked list and setting current node to the next node value
            current.set_next(new_node) # once we get to the end we will add the val in the parameter into the end of the linked list

    def display(self):
        """ Method to display nodes in the linked list"""
        current = self.head # initialize current pointer to head of linked list

        while current is not None: # Traverse over linked list and print value until there is none left in list
            print(current.value, end=" ") # print out current node
            current = current.get_next() # get next node for the loop

    def remove(self, pos):
        """ Method to remove the node at the specified position in the linked list """
        if self.head is None or pos < 0:  # Check if there is no size or head in the linked list, return nothing
            return

        if pos == 0:  # If the position is 0, remove the head
            removed_value = self.head.value  # Get the value of the removed head
            self.head = self.head.get_next()  # Assign the current head to the next value for the new head
            return self.head  # Return the new head

        current = self.head  # Initialize the current pointer to the head of the linked list
        previous = None  # Initialize the previous node variable
        count = 0  # Initialize count to track the position in the linked list

        while count < pos and current is not None:  # Iterate through the linked list until we reach the end
            previous = current  # Keep the previous as the current value as we iterate through the linked list
            current = current.get_next()  # Reassign the current node to the next node in the linked list
            count += 1  # Increment the count

        if current is not None:
            removed_value = current.value # initialize removed value
            previous.set_next(current.get_next()) # Update the next reference of the previous node to skip the node to be removed
            return removed_value # return the current node that gets removed

        

    def node_position(self, pos):
        """ Method to get the node at the specified position in the linked list """
        if pos < 0 or self.head is None: # if there is no head or negative position -- don't do anything
            return None # return nothing

        current = self.head # initialize current pointer to head of linked list
        count = 0 # initialize linked list count to track position

        while count < pos and current.get_next() is not None: # traverse the linkedlist until we get to the position needed
            current = current.get_next() # reassign current to traverse linked list
            count += 1 # increase count until we get to the position

        if count == pos: # check if we hit the position after the while loop
            return current # return new node value for linkedlist position
        else:
            return None # return nothing 

    def insert(self, val, pos):
        """ Insert a node with the given value into the specified position in the linked list """
        if pos < 0: # Check if the specified position is invalid
            print('Please use position 0 or greater.')

        new_node = Node(val)  # Initialize a new node with the given value

        if pos == 0: # Check to see if we are inserting at the beginning of the linked list
            new_node.next = self.head  # Set the next reference of the new node to the current head
            self.head = new_node  # Update the head to the new node

        else:
            current = self.head  # Initialize the current pointer to the head of the linked list
            count = 0  # Initialize count to track the position in the linked list

            while count < pos - 1 and current is not None: # Traverse the linked list to the node before the specified position
                current = current.next  # Move to the next node
                count += 1  # Increment the count to track the position

            if current is not None: # Check if the specified position is valid within the linked list
                new_node.next = current.next # Insert the new node between the current node and the next node
                current.next = new_node

def main():
    linked_list = LinkedList()

    # Test add method
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)

    print("Linked list contents:")
    linked_list.display()  # Output: 1 2 3 4
    print("\n")

    # Test get method for value within specific position
    print("node position 2:")
    print(linked_list.node_position(2).value)  # Output: 3
    print("node position with more than 4 nodes:")
    print(linked_list.node_position(4))  # Output: None (Starting count from index 0)
    print("\n")

    # Test remove method
    linked_list.remove(0)  # Remove head
    print("Remove head")
    linked_list.display()  # Output: 2,3,4
    print("\n")
    print("Remove at position 2:")
    linked_list.remove(2)  # Remove value 4 at position 2
    linked_list.display()  # Output: 2,3
    print("\n")

    print("Add nodes to end of linked list for values 4,5,6")
    linked_list.add(4)
    linked_list.add(5)
    linked_list.add(6)

    linked_list.display()  # Output: 2,3,4,5,6
    print("\n")

    # Test insert method
    print("Insert value 7 at head")
    linked_list.insert(7, 0) # Insert node at head
    linked_list.display() # Output: 7,2,3,4,5,6
    print("\n")

    print("Insert value 24 at position 5:")
    linked_list.insert(24, 5) # Insert node at position 5
    linked_list.display() # Output: 7,2,3,4,5,24,6
    print("\n")


if __name__ == "__main__":
    main()
