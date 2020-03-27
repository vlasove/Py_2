from collections import OrderedDict

d = {'a':20, 'b':30, 'c':50, 'w':20}
d = OrderedDict(sorted(d.items(), key=lambda t: (t[1])))
print(d)
d.popitem()