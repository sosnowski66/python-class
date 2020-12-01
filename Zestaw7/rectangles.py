from Zestaw7.points import Point


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2: raise ValueError("Podano nieprawidłowe wartości początkowe")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[({0}, {1}), ({2}, {3})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        x_center = (self.pt1.x + self.pt2.x) / 2
        y_center = (self.pt1.y + self.pt2.y) / 2
        return Point(x_center, y_center)

    def area(self):
        length = self.pt2.x - self.pt1.x
        height = self.pt2.y - self.pt1.y
        return length * height

    def move(self, x, y):
        x1 = self.pt1.x + x
        x2 = self.pt2.x + x
        y1 = self.pt1.y + y
        y2 = self.pt2.y + y
        return Rectangle(x1, y1, x2, y2)

    def intersection(self, other):
        a = self.pt1
        b = self.pt2
        c = other.pt1
        d = other.pt2

        x1 = max(a.x, c.x)
        y1 = max(a.y, c.y)
        x2 = min(b.x, d.x)
        y2 = min(b.y, d.y)

        if x1 > x2 or y1 > y2: return None

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        a = self.pt1
        b = self.pt2
        c = other.pt1
        d = other.pt2

        x1 = min(a.x, c.x)
        y1 = min(a.y, c.y)
        x2 = max(b.x, d.x)
        y2 = max(b.y, d.y)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        center = self.center()
        r1 = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        r2 = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
        r3 = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        r4 = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        return r1, r2, r3, r4