class Circle:
    R = 0
class Rectangle:
    A = 0
    B = 0 
def Ratio(c : Circle, r : Rectangle) -> bool:
    answer = (c.R * 2 <= r.A and c.R * 2 <= r.B) 
    return answer 
c = Circle()
c.R = 20
r = Rectangle()
r.A, r.B = 100, 200
print(Ratio(c,r))