from Zestaw7.Fracs import *
import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = Frac()

    def test_init(self):
        self.assertRaises(ValueError, Frac, 3, 0)

    def test_print(self):
        self.assertEqual(str(Frac(3, 1)), "3")
        self.assertEqual(str(Frac(1, 3)), "1/3")
        self.assertEqual(repr(Frac(1, 3)), "Frac(1, 3)")

    def test_cmp_frac(self):
        self.assertTrue(Frac(2, 3) < Frac(5, 6))
        self.assertTrue(Frac(2, 3) <= Frac(8, 12))
        self.assertTrue(Frac(4, 5) > Frac(2, 3))
        self.assertTrue(Frac(8, 12) >= Frac(2, 3))
        self.assertTrue(Frac(6, 9) == Frac(2, 3))
        self.assertTrue(Frac(2, 3) == Frac(2, 3))
        self.assertTrue(Frac(2, 3) != Frac(2, 4))

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(1, 2) + 1, Frac(3, 2))
        self.assertEqual(1 + Frac(1, 2), Frac(3, 2))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(1, 2) - 1, Frac(-1, 2))
        self.assertEqual(1 - Frac(1, 2), Frac(1, 2))

    def test_mul(self):
        self.assertEqual(Frac(2, 3) * Frac(3, 4), Frac(1, 2))
        self.assertEqual(Frac(2, 3) * 2, Frac(4, 3))
        self.assertEqual(2 * Frac(2, 3), Frac(4, 3))

    def test_div(self):
        self.assertEqual(Frac(2, 3) / Frac(3, 4), Frac(8, 9))
        self.assertEqual(Frac(2, 3) / 2, Frac(1, 3))
        self.assertEqual(2 / Frac(3, 4), Frac(8, 3))

    def test_one_argument_operators(self):
        self.assertEqual(+Frac(2, 3), Frac(2, 3))
        self.assertEqual(+Frac(2, 3), Frac(-2, -3))
        self.assertEqual(-Frac(2, 3), Frac(-2, 3))
        self.assertEqual(-Frac(2, 3), Frac(2, -3))
        self.assertEqual(~Frac(2, 3), Frac(3, 2))

    def test_float_frac(self):
        self.assertEqual(float(Frac(2, 3)), 2 / 3)


if __name__ == '__main__':
    unittest.main()
