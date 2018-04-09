import math
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getX(self):
    return self.x

  def getY(self):
    return self.y

class Line:
  def __init__(self, m, n):
    # print(x.__class__.__name__)
    # print(y.__class__.__name__)
    self.m = m
    self.n = n

  def length(self):
    return math.sqrt(pow(self.m.getX() - self.n.getX(), 2) + pow(self.m.getY() - self.n.getY(), 2))

a = Point(1.0, 2.0)
b = Point(2.0, 3.0)
line = Line(a, b)
dist = line.length()

print("dist:", dist)