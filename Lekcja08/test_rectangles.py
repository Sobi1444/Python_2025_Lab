import pytest
from rectangles import Point, Rectangle

def test_rectangle_from_points():
    p1 = Point(2, 3)
    p2 = Point(7, 8)
    rect = Rectangle.from_points((p1, p2))

    assert rect.left == 2
    assert rect.bottom == 3
    assert rect.right == 7
    assert rect.top == 8
    assert rect.width == 5
    assert rect.height == 5
    assert rect.topleft.x == 2
    assert rect.topleft.y == 8
    assert rect.bottomright.x == 7
    assert rect.bottomright.y == 3
    center = rect.center
    assert center.x == 4.5
    assert center.y == 5.5