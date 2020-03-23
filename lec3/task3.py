class Rectangle:
    A = 0
    B = 0 
    def perimeter(self):
        return (self.A + self.B) * 2

    def area(self):
        return self.A * self.B
r = Rectangle()
r.A = 200
r.B = 300
r.perimeter()


