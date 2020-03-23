a_list = [1,2,23,34,4,5]
b_tuple = (1,2,3,4,5,6)

a_list.append(20)

c = a_list[:]
c[0] = 200
print(c , a_list)

c1 = [1]
d1 = (1,)

print(type(c1))
print(type(d1))