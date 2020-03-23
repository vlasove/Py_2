a1 = set([1,2,3,4,5])
b1 = set([3,4,5,6,7,8])


c1 = a1.union(b1)
c2 = a1.intersection(b1)

c3 = a1 - b1 
c4 = b1 - a1 

print(c3 == c4)

if not 4 in c1:
    print("YESS")