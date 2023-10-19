import math

class Triangle():
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def perimeter(self):
        if len(self.points) != 3:
            return 0
        side1 = math.sqrt((self.points[1][0] - self.points[0][0]) ** 2 + (self.points[1][1] - self.points[0][1]) ** 2)
        side2 = math.sqrt((self.points[2][0] - self.points[0][0]) ** 2 + (self.points[2][1] - self.points[0][1]) ** 2)
        side3 = math.sqrt((self.points[2][0] - self.points[1][0]) ** 2 + (self.points[2][1] - self.points[1][1]) ** 2)
        return side1 + side2 + side3
    
    def is_equal(self, other_triangle):
        return sorted(self.points) == sorted(other_triangle.points)

    def __eq__(self, other_triangle):
        return sorted(self.points) == sorted(other_triangle.points)

    


t1 = Triangle()
t1.add_point(0, 0)
t1.add_point(0, 3)
t1.add_point(4, 0)


perimeter_t1 = t1.perimeter()
print("Perimeter of t1:", perimeter_t1)


t2 = Triangle()
t2.add_point(1, 2)
t2.add_point(2, 1)
t2.add_point(1, 5)


perimeter_t2 = t2.perimeter()
print("Perimeter of t2:", perimeter_t2)

are_equal = t1.is_equal(t2)
print("Are t1 and t2 equal:", are_equal)


t3 = Triangle()
t3.add_point(1, 2)
t3.add_point(2, 1)
t3.add_point(1, 5)


equal1 = t1 == t3
print("t1 == t3:", equal1)


equal2 = t1.__eq__(t3)
print("equlal or not :", equal2)

