class Reverse:
    def __init__(self, data):  # Fixed __init__ method
        self.data = data
        self.index = len(data)

    def __iter__(self):  # Fixed __iter__ method
        return self

    def __next__(self):  # Fixed __next__ method
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Testing the Reverse class
rev = Reverse('giraffe')
for char in rev:
    print(char)

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")
