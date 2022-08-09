# main exercises
#
import math


class MyFirstClass:
    pass


class Point:

    def reset(self):
        self.x = 0
        self.y = 0

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other:"Point"):
        return math.hypot(self.x - other.x,self.y - other.y)

    pass


a = MyFirstClass()
b = MyFirstClass()

print(a)
print(b)

print("are a and b the same in memory:", a is b)

point1 = Point()
point1.x = 20
point1.y = 10

point2 = Point()
point2.x = -45
point2.y = 28

print(point2.distance(point1))


