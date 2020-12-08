from Zestaw6.times import Time
import unittest

class TestTime(unittest.TestCase):

    # def setUp(self): pass

     # test str() i repr()
    def test_print(self):
        self.assertEqual(str(Time(3)), "00:00:03")
        self.assertEqual(repr(Time(3)), "Time(3)")
        self.assertNo

    def test_cmp(self):
        # Trzeba sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time(2) == Time(2))
        self.assertFalse(Time(2) == Time(3))
        self.assertTrue(Time(2) != Time(3))
        self.assertFalse(Time(2) != Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertFalse(Time(4) < Time(3))
        self.assertTrue(Time(2) <= Time(3))
        self.assertFalse(Time(4) <= Time(3))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertFalse(Time(2) >= Time(3))

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))

if __name__ == "__main__":
    unittest.main()     # wszystkie testy
