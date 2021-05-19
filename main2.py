class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side
    def Area(self):
        print("Iam : " + self.name +"\n"+
              "I have" + self.side + "sides")
obj_shape=Shapes("shape", "so many")
obj_shape.Area()

class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.legnth = len1
        self.width = wid1
    def Area(self):
        result= self.legnth * self.width
        return result
obj_book=Rectangle(10,7)
obj_screen = Rectangle(5, 7)
print("the area of  book is" + str(obj_book.Area()))
print("the area of  screen is" + str(obj_screen.Area()))

class Circle(Shapes):
    def __init__(self, circumfrence, pi):
        self.c = circumfrence
        self.pi = 3.14
    def Area(self):
        result = self.c / self.pi*2
        return result
obj_pen = Circle(2, 5)
print("the area of a pen is %.2f" + str(obj_pen.Area()))

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def Area(self):
        result = 1/2*self.base * self.height
        return result
obj_tri = Triangle(10,5)
print("the area of tri is" + str(obj_tri.Area()))
