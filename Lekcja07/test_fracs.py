import unittest
from fracs import Frac

class TestFrac(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Frac(1,2) + Frac(1,2), Frac(1,1))

    def test_sub(self):
        self.assertEqual(Frac(3,4) - Frac(1,4), Frac(1,2))

    def test_mul(self):
        self.assertEqual(Frac(2,3) * Frac(3,4), Frac(1,2))

    def test_div(self):
        self.assertEqual(Frac(1,2) / Frac(1,4), Frac(2,1))

    def test_float(self):
        self.assertAlmostEqual(float(Frac(1,2)), 0.5)

if __name__ == "__main__":
    unittest.main()