from Zestaw6.points import Point
import unittest


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.sample_point = Point(2, 4)

    def test_str(self):
        self.assertEqual(str(self.sample_point), "(2, 4)")
        self.assertEqual(repr(self.sample_point), "Point(2, 4)")

    def test_eq(self):
        self.assertTrue(self.sample_point == self.sample_point)
        self.assertTrue(self.sample_point == Point(2, 4))
        self.assertFalse(self.sample_point == Point(1, 4))
        self.assertFalse(self.sample_point == Point(2, 5))

    def test_ne(self):
        self.assertTrue(self.sample_point != Point(1, 4))
        self.assertTrue(self.sample_point != Point(2, 5))
        self.assertFalse(self.sample_point != self.sample_point)
        self.assertFalse(self.sample_point != Point(2, 4))

    def test_add_(self):
        self.assertEqual(self.sample_point + self.sample_point, Point(4, 8))
        self.assertEqual(Point(1, 2) + Point(3, 3), Point(4, 5))

    def test_sub(self):
        self.assertEqual(Point(6, 3) - Point(2, 7), Point(4, -4))
        self.assertEqual(Point(6, 3) - Point(2, 0), Point(4, 3))

    def test_mul(self):
        self.assertEqual(self.sample_point * Point(2, 0), 4)
        self.assertEqual(self.sample_point * Point(2, 3), 16)
        self.assertEqual(self.sample_point * Point(2, -3), -8)

    def test_cross(self):
        self.assertEqual(self.sample_point.cross(Point(2, 5)), 2)

    def test_length(self):
        from math import sqrt
        self.assertEqual(self.sample_point.length(), sqrt(20))


if __name__ == '__main__':
    unittest.main()