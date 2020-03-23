nums = []
for i in range(0,1001, 2):
    nums.append(i**2)

[x**2 if x % 3 == 0 else x **3 for x in range(0,1001,2) ]



#input:                       #output
# 2 3 4 5 6 7                   27
# 1 1                           2
# 3                             3
# 10 10 10                      30






print(sum([int(i) for i in input().split()]))

a = [] 
in_str = input()
for i in in_str.split():
    a.append(int(i))
print(sum(a))

d = {'one' : 1, None: 2, True:3, 22.33:4, (1,2,3) : 10}

d["four"] = 200

c = d.copy()
c['one'] = 1010101
print(c,d)
