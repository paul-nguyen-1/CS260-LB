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
        return self._marble_bag # return marble data

    def is_empty(self):
        """ Definition used to check if marble bag is empty """
        return not self._marble_bag # check if bag is not empty
    
    def display_marble_bag(self):
        """ Definition is used to display marble bag contents"""
        if not self.is_empty(): # check if marble mag is empty using our is_empty function
            return self._marble_bag
        else:
            print('Marble bag is empty') # if our conditional shows that we have an empty bag print to show user marble bag is empty
    
    def marble_bag_count(self):
        """ Definition is used to get the marble bag count"""
        count = 0 # initialize marble bag count
        for _ in self._marble_bag: # iterate over marble bag for amount of marbles
            count += 1 # incrememnt count for each marble
        return count # print out marble bag count

    def get_marble_count(self, color):
        """ Definition is used to get the marble color count in the bag"""
        count = 0  # initialize marble count
        if not self.is_empty(): # check if marble bag is not empty
            for marble in self._marble_bag: # iterate over marble in marble bag
                if marble["color"] == color: # check for key (color) inside dictionary
                    count += 1  # Increment count when a marble matches the specified color
        return count # print our count for marble color
    


if __name__ == "__main__":
    # Create a bag of marbles
    bag = BagOfMarbles()

    # Check for empty bag
    print(f"Bag is empty: {bag.is_empty()}")
    
    # Test adding marbles
    bag.add_marble("red", 4)
    bag.add_marble("blue", 5)
    bag.add_marble("green")
    
    # Print marble bag count: 10
    print(f"Blue marble count: {bag.get_marble_count('blue')}")
    print(f"Red marble count: {bag.get_marble_count('red')}")
    print(f"Green marble count: {bag.get_marble_count('green')}")
    # Check for not empty bag
    print(f"Bag is empty: {bag.is_empty()}")
    print(f"Marble bag count: {bag.marble_bag_count()}")

    # Make sure Red blue and green marbles are in the bag
    print(f"Marble Bags: {bag.display_marble_bag()}")

    # Test removing blue marble from the bag
    bag.remove_marble('blue', 3)
    print(f"Remove blue 3 marbles: {bag.get_marble_count('blue')}")
    
    # Check marble count for blue marble
    print(f"Blue marble count: {bag.get_marble_count('blue')}")
    print(f"Red marble count: {bag.get_marble_count('red')}")
    print(f"Green marble count: {bag.get_marble_count('green')}")
    print(f"Marble bag count: {bag.marble_bag_count()}")
    print(f"Marble Bags: {bag.display_marble_bag()}")
    
    # Test removing more than what we currently have in the bag
    print(f"Remove 50 red marbles: {bag.remove_marble('red', 50)}")
    print(f"Blue marble count: {bag.get_marble_count('blue')}")
    print(f"Red marble count: {bag.get_marble_count('red')}")
    print(f"Green marble count: {bag.get_marble_count('green')}")
    print(f"Marble count: {bag.marble_bag_count()}")
    print(f"Marble Bag: {bag.display_marble_bag()}")
    
    # Add 12 red marbles
    bag.add_marble('red', 12)
    print(f"Add 12 red marbles: {bag.get_marble_count('red')}")
    print(f"Blue marble count: {bag.get_marble_count('blue')}")
    print(f"Red marble count: {bag.get_marble_count('red')}")
    print(f"Green marble count: {bag.get_marble_count('green')}")
    print(f"Final marble count: {bag.marble_bag_count()}")
    print(f"Marble count: {bag.marble_bag_count()}")
    print(f"Marble Bag: {bag.display_marble_bag()}")

