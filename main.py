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

    def distance(self, other: "Point"):
        return ((self.x - other.x)**2 +  (self.y - other.y)**2)**(1/2)

    pass


a = MyFirstClass()
b = MyFirstClass()

print(a)
print(b)

print("are a and b the same in memory:", a is b)

x1 =
y1 =

x2 =
y2 =