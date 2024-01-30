#Implementation
class Node:
    # Initialize node values
    def __init__(self, value):
        self.value = value # Node value of Linked List
        self.next = None # Next node value on Linked List
 
class Queue:
    # Initializes queue values
    def __init__(self):
        self.head = None # Top value of queue
        self.tail = None # tail value of queue
        self.size = 0 # Size of queue
 
    def is_empty(self):
        return self.head == None # Check for head in queue -- if empty true, else false
        # return self.size == 0 # Alternatize if we want to check empty using size value
    
    # Method to insert an element into the head of the queue
    def enqueue(self, element):
        temp = Node(element) # New node stored with the value that will be added to the queue
 
        # Check if the queue is currently empty
        if self.is_empty():
            self.head = self.tail = temp  # If the queue is empty, the new node becomes both the head and tail
        else:
            self.tail.next = temp  # Link the current tail node to the new node
            self.tail = temp  # Update the tail pointer to the new node

        self.size += 1  # Increment the size of the queue
        return self.head # return head of queue
 
    # Method to remove an element from queue
    def dequeue(self):
        if self.is_empty(): # Check if queue is empty
            return None # return nothing if empty queue
        temp = self.head # temporary variable to hold the current head node
        self.head = temp.next # assign the head pointer to the next node in the queue
        self.size -= 1 # Remove node from linked list
        return temp.value  # Return the value of the dequeued node
    
    
    def peek_top(self):
        if self.is_empty(): # Check if linked list is empty
            return None  # Return none if linked list is empty
        return self.head.value # Return top value if linked list is not empty
    
    def check_size(self):
        return self.size # Return size of linked list
    

#Testing
if __name__ == "__main__":
    my_queue = Queue()
    
    # Test enqueue
    print("Add nodes to linked list ----------------------")
    my_queue.enqueue('top node')
    my_queue.enqueue('middle node')
    my_queue.enqueue('bottom node')
    print(f"Print out top queue: {my_queue.peek_top()}")  # should print out top node
    print(f"Print out size: {my_queue.check_size()}")  # should print out 3
    
    # Test dequeue
    print("Remove a node from linked list -----------------")
    print(f"Removed:{my_queue.dequeue()} from the queue") # Should print out top node removed
    print(f"Print out top queue: {my_queue.peek_top()}")  # should print out middle node
    print(f"Print out size: {my_queue.check_size()}")  # should print out 2
    