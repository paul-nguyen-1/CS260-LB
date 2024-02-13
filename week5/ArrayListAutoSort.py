class ArrayList:
    def __init__(self) -> None:
        """ Initialize array list """
        self.array_list = []

    def insert(self, value) -> None:
        """ Insert an element into the array list in ascending order.
            value: integer
        """
        index = 0  # Initialize index to check where to put value
        while index < len(self.array_list) and self.array_list[index] < value:
            # Loop over array list until we get to the end of the list and check
            # as we iterate over the list that we increment our index until we reach
            # a value greater than the one we are inserting
            index += 1  # Incrementing our index
        self.array_list.insert(index, value)  # Insert the value at the correct position based on the index

    def search(self, value) -> None:
        """ Set up binary search for array list.
            value: integer
        """
        
        # Low is the lower boundary (0) and high is the upper boundary (last element in list)  -- Two Pointers
        low, high = 0, len(self.array_list) - 1

        while low <= high: 
            mid = (low + high) // 2

            if self.array_list[mid] == value: # check if we reached the correct value index
                return mid # return position of value
            elif self.array_list[mid] < value: # since value is at lower boundary we will increment the left pointer
                low = mid + 1 # increment lower boundary
            else: # since the value is at the upper boundary we will decrement the right pointer
                high = mid - 1 # decrement upper boundary

        print(f"{value} not found in the array list")

    
    # Just doing this function for funsies
    def remove(self, value) -> None:
        """ Deletion of an element from the array list.
            value: Integer
        """
        if value in self.array_list:
            # Check if value is inside our list and remove it from our array list
            self.array_list.remove(value)  # Remove value from list

    def display(self) -> None:
        """ Display array list """
        print(self.array_list)
