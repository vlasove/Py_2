A,B,C = int(input()), int(input()), int(input())

if A == 0 :
    #BX + C = 0 --> x = -c/b
    if B == 0:
        print()
    else:
        print('X: %.2f'%(-C/B))
else:
    D = B**2 - 4*A*C  
    if D > 0:
        x1,x2 = ...
    elif D == 0:
        x = ... 
    else:
        print()