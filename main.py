class Arrays:
    def __init__(self, size, default_value=None):
        self.size = size
        self.items = list()
        if default_value is None:
            for i in range(size):
                self.items.append(default_value)

        else:
            if (len(default_value) == size) or (len(default_value) < size):
                for j in default_value:
                    self.items.append(j)
                for j in range(len(default_value), size):
                    self.items.append(None)

            if len(default_value) > size:
                print("Error! Elements are more than the size of the array.")

    """This function returns the number of the elements in an array, excluding the None values if there are any."""

    def my_len(self):
        length = 0
        for i in self.items:
            if i is None:
                continue
            else:
                length += 1

        return length

    """This function inserts the element at the last"""

    def insert_last(self, item):
        if self.my_len() < self.size:
            self.items.append(item)
        else:
            print("Error! Element index out of range.")

    """This function inserts the element at the beginning of an array."""

    def insert_first(self, element):
        if self.my_len() < self.size:
            for i in range(self.my_len(), 0, -1):
                self.items[i] = self.items[i - 1]
            self.items[0] = element
        else:
            print("Error! Element index out of range.")

    """This function inserts the element at the given index in an array"""

    def insert_at_index(self, index, element):
        if (self.my_len()) < self.size:
            for i in range(self.my_len(), index, -1):
                self.items[i] = self.items[i - 1]
            self.items[index] = element
        else:
            print("Error! Element index out of range.")

    """This function removes the element at the given index in an array"""
    def remove_at_index(self, index):
        for i in range(index, self.my_len() - 1, 1):
            self.items[i] = self.items[i + 1]
        self.items[self.my_len()-1] = None

    def print(self):
        print(self.items)


