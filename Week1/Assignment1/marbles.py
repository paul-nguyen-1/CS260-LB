class BagOfMarbles:
    """ Initialize BagOfMarbles class """
    def __init__(self):
        """ Initialize marble bag """
        self._marble_bag = [] # initialize marble bag into an array/list

    def add_marble(self, color, amount=1): # color variable in parameter is used to check what marble color we would like to add, default amount of marbles added is 1
        """ Definition used to add marble color and amount to marble bag """
        for _ in range(amount):  # Use a loop to add the specified amount of marbles
            self._marble_bag.append({"color": color}) # Append marble color dictionary into our array with the amount

    def remove_marble(self, color, amount=1):
        """ Definition used to remove marble color and amount to marble bag """
        new_marble_bag = []  # Create a new list to store marbles without the specified color
        removed_count = 0  # Counter for the number of removed marbles

        for marble in self._marble_bag: # iterate over marble
            if marble["color"] == color and removed_count < amount: # conditional to check for marble removed color and adds marbles remaining that were not removed to the new marble bag
                removed_count += 1 # our counter for the removed marbles
            else:
                new_marble_bag.append(marble) # append remaining marbles not removed to new bag

        self._marble_bag = new_marble_bag # old bag data will be overwritten with the the new marble bag data

    def is_empty(self):
        """ Definition used to check if marble bag is empty """
        if not self._marble_bag: # check if marble bag is empty
            return False # if bag is empty remove
    
    def display_marble_bag(self):
        """ Definition is used to display marble bag contents"""
        if not self.is_empty(): # check if marble mag is empty using our is_empty function
            for marble in self._marble_bag: # iterate over marbles in marble bag
                print(f"Current marbles in the bag:", marble) # display all the marbles inside the marble bag
        else:
            print('Marble bag is empty') # if our conditional shows that we have an empty bag print to show user marble bag is empty
    
    def marble_bag_count(self):
        """ Definition is used to get the marble bag count"""
        count = 0 # initialize marble bag count
        for _ in self._marble_bag: # iterate over marble bag for amount of marbles
            count += 1 # incrememnt count for each marble
        print(count) # print out marble bag count

    def get_marble_count(self, color):
        """ Definition is used to get the marble color count in the bag"""
        count = 0  # initialize marble count
        if not self.is_empty(): # check if marble bag is not empty
            for marble in self._marble_bag: # iterate over marble in marble bag
                if marble["color"] == color: # check for key (color) inside dictionary
                    count += 1  # Increment count when a marble matches the specified color
        print(count) # print our count for marble color
    


if __name__ == "__main__":
    # Create a bag of marbles
    bag = BagOfMarbles()

    # Check for empty bag
    print(bag.is_empty())
    # Test adding marbles
    bag.add_marble("red")
    bag.add_marble("blue")
    bag.add_marble("green")

    # Make sure Red blue and green marbles are in the bag
    bag.display_marble_bag()

    # Test removing green marble from the bag
    bag.remove_marble("green")
    print('Green marble removed')
    bag.display_marble_bag()
    
    # Get marble bag count
    bag.marble_bag_count()

    # Get marble color count in marble bag
    bag.get_marble_count('red')
