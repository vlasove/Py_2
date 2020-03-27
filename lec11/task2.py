from collections import Counter

c = Counter(a=2, b=2, c=4, d= -2)
d = Counter(a=2,b=20, c=30, d= 10)
print(c.subtract(d))
print(c)

#c.clear()
dict(c)
print(list(c))