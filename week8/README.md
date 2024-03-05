# Hashtable Implementation

## Simple Hashtable

### Design:

1. **Hashing Function:**
   - Utilizes the modulo operation to determine the index for each key

2. **Insert Function:**
   - Calculate the hash index using the hashing function
   - If the index is vacant, insert a new node with the given key and value
   - If the index is occupied, traverse the linked list at that index, update the value if the key exists, or append a new node at the end

3. **Contains Function:**
   - Calculate the hash index using the hashing function
   - Traverse the linked list at the calculated index to check if the key exists

4. **Delete Function:**
   - Calculate the hash index using the hashing function
   - Traverse the linked list at the calculated index to find the node with the specified key and removes it

### Unit Tests:

#### Insert and Contains Test:

- Initialize Hashtable
- Insert values
- Verify contains function

#### Delete Key Test:

- Initialize Hashtable
- Insert values
- Delete key 1
- Verify contains function

## Double Hashing Hashtable

### Design:

1. **Hashing Function:**
   - Uses the modulo operation to determine the primary hash index

2. **Secondary Hash Function (Double Hashing):**
   - Implement a secondary hash function to calculate the step size for probing during collisions

3. **Insert Function:**
   - Calculate the primary hash index using the hashing function
   - If the index is vacant, insert a new node with the given key and value
   - If the index is occupied, use double hashing to find the next available index and insert the new node

4. **Contains Function:**
   - Calculate the primary hash index using the hashing function
   - Use double hashing to traverse the array and find the key or an empty slot

5. **Delete Function:**
   - Calculate the primary hash index using the hashing function
   - Uses double hashing to traverse the array and find the node with the specified key and remove it

### Unit Tests:
    - TestHashtable.py lines 1-47

#### Insert and Contains Test:

- Initialize Hashtable
- Insert values
- Verify contains function

#### Delete Key Test:

- Initialize Hashtable
- Insert values
- Delete key 11
- Verify contains function

# Simple Hashtable

### Insertion Complexity:

- **Without Collisions:** O(1) - In an ideal scenario with no collisions, the insert operation is constant time.

- **With Collisions:** O(1) to O(n) - Resolving collisions adds complexity. In the worst case the time complexity can degrade to O(n), where n is the number of keys.

### Contains Complexity:

- **Without Collisions:** O(1) - In an ideal case with no collisions, the contains operation is constant time.

- **With Collisions:** O(1) to O(n) - The worst-case time complexity for contains is affected by collisions. It can approach O(n) in the worst case due to the need to resolve collisions.

# Double Hashing Hashtable

### Insertion Complexity:

- **Without Collisions:** O(1) - In an ideal scenario with no collisions, the insert operation is constant time.

- **With Collisions:** O(1) to O(n) - Resolving collisions adds complexity. In the worst case, the time complexity can degrade to O(n), where n is the number of keys.

### Contains Complexity:

- **Without Collisions:** O(1) - In an ideal case with no collisions, the contains operation is constant time.

- **With Collisions:** O(1) to O(n) - The worst-case time complexity for contains is affected by collisions. It can approach O(n) in the worst case due to the need to resolve collisions.
