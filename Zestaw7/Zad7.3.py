from Zestaw7.rectangles import *
import unittest


class TestRectangle(unittest.TestCase):

    def setUp(self): pass

    def test_create_rect(self):
        self.assertRaises(ValueError, Rectangle, 4, 5, 2, 7)

    def test_print(self):
        self.assertEqual(str(Rectangle(2, 3, 5, 7)), "[(2, 3), (5, 7)]")
        self.assertEqual(repr(Rectangle(2, 3, 5, 7)), "Rectangle(2, 3, 5, 7)")

    def test_cmp_rect(self):
        self.assertTrue(Rectangle(0, 0, 5, 4) == Rectangle(0, 0, 5, 4))
        self.assertTrue(Rectangle(0, 0, 5, 4) != Rectangle(0, 0, 1, 3))

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 10, 6).center(), Point(5, 3))

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 10, 6).move(1, 1), Rectangle(1, 1, 11, 7))

    def test_intersection(self):
        self.assertEqual(Rectangle(0, 0, 10, 6).intersection(Rectangle(4, 1, 12, 3)), Rectangle(4, 1, 10, 3))

    def test_cover(self):
        self.assertEqual(Rectangle(0, 0, 10, 6).cover(Rectangle(4, 1, 12, 3)), Rectangle(0, 0, 12, 6))

    def test_make4(self):
        self.assertEqual(Rectangle(0, 0, 10, 6).make4(), (Rectangle(0, 0, 5, 3), Rectangle(5, 0, 10, 3), Rectangle(0, 3, 5, 6), Rectangle(5, 3, 10, 6)))


if __name__ == '__main__':
    unittest.main()