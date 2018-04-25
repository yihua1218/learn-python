import json
class MyCar:
  total = 0
  __color = ''

  def __init__(self, color):
    MyCar.total = MyCar.total + 1
    self.__color = color

  def __del__(self):
    MyCar.total = MyCar.total - 1
  
  def show(self):
    print(self.__color)

  def getColor(self):
    return(self.__color)

  @classmethod
  def howManyCars(cls):
    return cls.total

red = MyCar("red")
green = MyCar("green")
yellow = MyCar("yellow")

print(MyCar.total)
print(red.getColor())
print(green.getColor())

print(MyCar.howManyCars())

red.show()

del red

print(MyCar.howManyCars())

# MyCar.show()

# print(green.__dict__)
# json.dump(red, "red.car")
green_file = open("green.car", "w")
yellow_file = open("yellow.car", "w")
json.dump(green.__dict__, green_file)
json.dump(yellow.__dict__, yellow_file)