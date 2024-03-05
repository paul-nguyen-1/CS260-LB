class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        
class Hashtable:
    def __init__(self, initial_size) -> None:
        """
        Initialize a Hashtable

        Args:
        - initial_size: Initial size of the hashtable
        """
        self.size = initial_size
        self.table = [None] * initial_size
        self.collision = 0

    def index(self, key: int) -> int:
        """
        Calculate the hash index for the given key using the modulo operation

        Args:
        - key: The key for which the hash index needs to be calculated

        """
        return key % self.size

    def insert(self, key: int, value: int) -> None:
        """
        Insert a key-value pair into the hashtable

        Args:
        - key: The key to be inserted.
        - value: The corresponding value for the key
        """
        index = self.index(key)
        if not self.table[index]: # If there's no hashtable present, create a hashtable and add the key,value
            self.table[index] = Node(key, value)
            return
        current = self.table[index]
        while current: # Iterate through the hashtable
            if current.key == key: # Check if the current node has the desired key
                current.value = value # Reassign new key value
                return
            if not current.next: # If there's no hashtable present, create a hashtable and add the key,value
                current.next = Node(key, value)
                return
            current = current.next # Keep iterating through the hashtable

    def contains(self, key: int) -> int:
        """
        Check if the hashtable contains a key and return its corresponding value

        Args:
        - key: The key to be checked
        """
        index = self.index(key)
        current = self.table[index]
        while current: # Iterate through the hashtable
            if current.key == key: # Check if the current node has the desired key
                return current.value # Return value
            current = current.next # Keep iterating through the hashtable
        return 'not found'

    def delete(self, key: int) -> None:
        """
        Delete a key-value pair from the hashtable based on the key

        Args:
        - key: The key to be deleted
        """
        index = self.index(key)
        current = self.table[index] # Get the hashtable at the calculated index
        if not current: # If the linked list is empty, no deletion is needed
            return
        if current.key == key: # If the first node in the linked list has the desired key, remove it
            self.table[index] = current.next
            return
        while current.next: # Iterate through the linked list to find the node with the specified key
            if current.next.key == key: # If the next node has the desired key, remove it by updating the next reference
                current.next = current.next.next
                return
            current = current.next # Move to the next node in the linked list


class DoubleHashingHashtable:
    def __init__(self, initial_size) -> None:
        """
        Initialize a Double Hashing Hashtable

        Args:
        - initial_size: Initial size of the hashtable
        """
        self.size = initial_size
        self.table = [None] * initial_size
        self.collision = 0

    def index(self, key: int) -> int:
        """
        Calculate the primary hash index for the given key

        Args:
        - key: The key for which the hash index needs to be calculated
        """
        return key % self.size

    def second_hash_function(self, key: int, prime: int) -> int:
        """
        Calculate the secondary hash value using a given prime number

        Args:
        - key: The key for which the secondary hash needs to be calculated
        - prime: A prime number used in the secondary hash calculation

        Returns:
        - int: The secondary hash value
        """
        return prime - (key % prime)

    def insert(self, key: int, value: int) -> None:
        """
        Insert a key-value pair into the hashtable using double hashing

        Args:
        - key: The key to be inserted
        - value: The corresponding value for the key
        """
        index = self.index(key)
        if not self.table[index]:  # If the index is vacant, insert the node directly
            self.table[index] = Node(key, value)
        else: # Collision occurred -- use double hashing
            step_size = self.second_hash_function(key, self.size)  # Pass the 'prime' argument
            current_index = (index + step_size) % self.size

            while self.table[current_index]: # Resolve collisions using double hashing
                if self.table[current_index].key == key: # If the key is already present, update the value
                    self.table[current_index].value = value
                    return
                self.collision += 1
                current_index = (current_index + step_size) % self.size
            self.table[current_index] = Node(key, value) # If the index is vacant after resolving collisions, insert the node

    def contains(self, key: int) -> int:
        """
        Check if the hashtable contains a key and return its corresponding value

        Args:
        - key: The key to be checked
        """
        index = self.index(key)
        step_size = self.second_hash_function(key, self.size)  # Pass the required 'prime' argument
        current_index = index

        while self.table[current_index]:
            if self.table[current_index].key == key:
                return self.table[current_index].value
            current_index = (current_index + step_size) % self.size

        return 'not found'

    def delete(self, key: int, prime: int) -> None:
        """
        Delete a key-value pair from the hashtable based on the key

        Args:
        - key: The key to be deleted
        - prime: A prime number used in the secondary hash
        """
        index = self.index(key)
        step_size = self.second_hash_function(key, prime)
        current_index = index

        while self.table[current_index]:
            if self.table[current_index].key == key:  # If the key is found, remove the corresponding node
                self.table[current_index] = None
                return
            current_index = (current_index + step_size) % self.size
