temp = [1,2,3,4,5,6,7,78,98]
print('Iinitial size:', temp.__sizeof__())
temp.pop()
print('After pop size:', temp.__sizeof__())
temp.pop()
temp.pop()
temp.pop()
temp.pop()
temp.pop()
print('After double pop size:', temp.__sizeof__())

fqweq = 12.121212121212
print('Floating: %.2f'%fqweq)
