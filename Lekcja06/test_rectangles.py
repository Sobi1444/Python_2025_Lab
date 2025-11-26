import unittest
from rectangles import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(0, 0, 2, 3)
        self.r2 = Rectangle(1, 1, 3, 4)

    def test_str_repr_eq(self):
        self.assertEqual(str(self.r1), "[(0, 0), (2, 3)]")
        self.assertEqual(repr(self.r1), "Rectangle(0, 0, 2, 3)")
        self.assertTrue(self.r1 == Rectangle(0, 0, 2, 3))
        self.assertFalse(self.r1 == self.r2)
        self.assertTrue(self.r1 != self.r2)

    def test_center_area_move(self):
        self.assertEqual(self.r1.center(), Point(1, 1.5))
        self.assertEqual(self.r1.area(), 6)
        self.r1.move(1, 2)
        self.assertEqual(self.r1.pt1, Point(1, 2))
        self.assertEqual(self.r1.pt2, Point(3, 5))

if __name__ == "__main__":
    unittest.main()