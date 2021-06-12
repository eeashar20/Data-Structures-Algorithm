class Arrays:
    def __init__(self, size, default_value = None):
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

    def __str__(self):
        print(self.items)


number = Arrays(8, [1, 2, 3, 4, 5])

# print(number.size)
print(number)
