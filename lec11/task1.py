import collections

#collections.Counter() - dict() + количество объектов
c = collections.Counter()

for word in ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'a']:
    c[word] += 1

print(c)
print(c['a'])

print(list(c.elements()))
print(c.most_common(0))