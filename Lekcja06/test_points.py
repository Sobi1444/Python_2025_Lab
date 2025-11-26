import unittest
from points import Point

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(3, 4)
        self.p2 = Point(1, 2)

    def test_str_repr_eq(self):
        self.assertEqual(str(self.p1), "(3, 4)")
        self.assertEqual(repr(self.p1), "Point(3, 4)")
        self.assertTrue(self.p1 == Point(3, 4))
        self.assertFalse(self.p1 == self.p2)
        self.assertTrue(self.p1 != self.p2)

    def test_operations(self):
        self.assertEqual(self.p1 + self.p2, Point(4, 6))
        self.assertEqual(self.p1 - self.p2, Point(2, 2))
        self.assertEqual(self.p1 * self.p2, 3*1 + 4*2)
        self.assertEqual(self.p1.cross(self.p2), 3*2 - 4*1)
        self.assertAlmostEqual(self.p1.length(), 5.0)

if __name__ == "__main__":
    unittest.main()