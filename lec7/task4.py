class Rectangle:
    def __init__(self, a=0, b=0):
        self.__a = a
        self.__b = b 

    def perimeter(self):
        return 2*(self.__a + self.__b)

class Circle:
    def __init__(self, r= 0):
        self.__r = r 

    def perimeter(self):
        return 2* 3.14 * self.__r

class Sphere(str, dict, Circle):
    def volume(self):
        return 4/3 * 3.14 * self.__r**3


r = Rectangle(10, 20)
print(r.perimeter())
c = Circle(200)
print(c.perimeter())

s = Sphere(10)
print(s.perimeter())