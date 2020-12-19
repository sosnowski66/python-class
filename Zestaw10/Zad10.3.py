class Stack:

    def __init__(self, size=100):
        self.size = size
        self.items = [None] * size
        self.added_numbers = [False] * size

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):                  # nigdy nie jest pełny
        return len(self.items) == self.size

    def push(self, item):
        if len(self.items) != self.size and not self.added_numbers[item]:
            self.items.append(item)         # dodajemy na koniec
            self.added_numbers[item] = True

    def pop(self):      # zwraca element
        if not self.is_empty():
            deleted = self.items.pop()         # zabieram od końca
            self.added_numbers[deleted] = False
            return deleted