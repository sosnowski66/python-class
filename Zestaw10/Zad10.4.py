import unittest

class Queue:

    def __init__(self, maxSize=10):
        self.items = []
        self.size = maxSize

    def __str__(self):             # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):             # nigdy nie jest pusta
        return len(self.items) >= self.size

    def put(self, data):
        if self.is_full():
            raise Exception("Peny stos")
        else:
            self.items.append(data)

    def get(self):
        if self.is_empty():
            raise Exception("Pusty stos!")
        else:
            return self.items.pop(0)   # mało wydajne!


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_str(self):
        self.assertEqual(str(self.queue), '[]')

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)

    def test_is_full(self):
        self.queue.put(0)
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(3)
        self.queue.put(4)
        self.queue.put(5)
        self.queue.put(6)
        self.queue.put(7)
        self.queue.put(8)
        self.queue.put(9)
        self.assertEqual(self.queue.is_full(), True)
        self.assertEqual(Queue().is_full(), False)

    def test_pop(self):
        with self.assertRaises(Exception):
            self.queue.get()
        self.queue.put(1)
        self.assertEqual(self.queue.get(), 1)

    def test_put(self):
        self.queue.put(3)
        self.queue.put(5)
        self.queue.put(7)
        self.queue.put(0)
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(3)
        self.queue.put(4)
        self.queue.put(5)
        self.queue.put(6)
        with self.assertRaises(Exception):
            self.queue.put(7)
        self.assertAlmostEqual(self.queue.get(), 3)
        self.assertAlmostEqual(self.queue.get(), 5)
        self.assertAlmostEqual(self.queue.get(), 7)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy