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
    @property
    def my_len(self):
        length = 0
        for i in self.items:
            if i is None:
                continue
            else:
                length += 1

        return length

    def __str__(self):
        print(self.items)


