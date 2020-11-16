from Zestaw5.fracs import *
import unittest

f1 = [-1, 2]  # -1/2
f2 = [0, 1]  # zero
f3 = [3, 1]  # 3
f4 = [6, 2]  # 3 (niejednoznaczność)
f5 = [0, 2]  # zero (niejednoznaczność)


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([4, 2], [1, 3]), [2, 3])

    def test_div_frac(self):
        self.assertEqual(div_frac([4, 2], [1, 3]), [6, 1])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([1, -2]), False)
        self.assertEqual(is_positive([-1, -2]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero(f2), True)
        self.assertEqual(is_zero(f5), True)
        self.assertEqual(is_zero(f3), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(f2, f5), 0)
        self.assertEqual(cmp_frac(f3, f4), 0)
        self.assertEqual(cmp_frac(f1, f2), -1)
        self.assertEqual(cmp_frac(f1, f3), -1)
        self.assertEqual(cmp_frac(f3, f1), 1)
        self.assertEqual(cmp_frac(f3, f2), 1)

    def test_frac2float(self):
        self.assertIsInstance(type(frac2float([1, 3])), float.__class__)
        self.assertEqual(frac2float(f1), -0.5)
        self.assertEqual(frac2float([1, 3]), 1/3)


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
