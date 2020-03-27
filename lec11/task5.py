from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y = 2)
print(p)
print(p.x)
print(p.y)
print(p[0])