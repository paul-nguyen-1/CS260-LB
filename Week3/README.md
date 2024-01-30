<h1>Based on what we know about linked lists, stacks, and queues, design a linked queue</h1>
<h2>Functions used in Linked Queue Data Structure</h2>
<ol>
<li>Enqueue(x) (O1): Insertion. We will take an element as a parameter for the enqueue function and add the value of the element to the back of the queue.</li>
<li>Dequeue() (O1): Deletion. We will remove the element from the front of the queue and return the value that is removed.</li>
<li>PeekTop() (O1): We will create a function that will return the value at the front of the queue (without removing it).</li>
<li>Check Size() (O1): Check the size of the queue to keep track of how many nodes are currently present in linked queue. </li>
<li>Is Empty() (O1): Check whether queue is empty or not. We will check the linked list and validate if the queue is empty.</li>
</ol>
<h2>Values used in Linked Queue Data Structure</h2>
<ol>
<li>Head: The head of the linked list points to the front of the queue. It keeps track of the first element in the queue.</li>
<li>Tail: The tail of the linked list points to the back of the queue. It keeps track of the last element in the queue.</li>
<li>Size of the queue. It keeps track of the queue size when we add or delete a node.</li>
</ol>

<h2> Implementation Complexities </h2>
<ol>
<li>Enqueue (O1): Enqueue function involves creating a new node and updating the tail pointer. This functions is constant time since it does not depend on the size of the queue.</li>
<li>Dequeue (O1): Dequeue function involves updating the head pointer. This function is constant time since it does not depend on the size of the queue.</li>
<li>PeekTop (O1): Peek top operation returns the value of the head node. It is a constant time operation since it does not depend on the size of the queue unless it is empty.</li>
<li>CheckSize (O1): The size of the queue is maintained as a variable, so checking the size is a constant time operation.</li>
<li>IsEmpty (O1): Check's whether or not there is a node at the head of the linked list, so checking the queue is a constant time operation. </li>
</ol>

<h1>Diagram of Values:</h1>
![](uml.png)

<h1>Testing Implementation:</h1>
![](testing.png)