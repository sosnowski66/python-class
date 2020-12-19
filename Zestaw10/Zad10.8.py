import random

class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        return str(self.items)

    def remove(self):    # zwraca losowy element
        if self.is_empty():
            raise ValueError("Uwaga - pusta kolejka")
        index = self.random.randint(0,len(self.items) - 1)
        self.items[index], self.items[-1] = self.items[-1], self.items[index]
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):     # czyszczenie listy
        self.items = []