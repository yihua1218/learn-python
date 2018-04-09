
class Humen:
  sexal = 'unknow'
  age = 0
  first_name = ''
  last_name = ''

  def __init__(self, sexal, age, first_name, last_name):
    self.sexal = sexal
    self.age = age
    self.first_name = first_name
    self.last_name = last_name

  def hello(self):
    print("Hello, I am", self.last_name, self.first_name)


class Student(Humen):
  degree = 1

  def __init__(self, sexal, age, first_name, last_name):
    super().__init__(sexal, age, first_name, last_name)

  def hello(self):
    super().hello()
    print("I am at degree", self.degree)

  def hi(self):
    self.hello()

tom = Humen('male', 18, 'Tom', 'Jackson')
tom.hello()

del tom

marry = Student('female', 15, 'Marry', 'King')
marry.hello()
marry.hi()
