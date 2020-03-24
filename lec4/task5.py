def linear(B : int,C : int) -> int :
    if B == 0:
        return 0
    else:
        return 1

def squarer(A : int,B : int, C : int)-> int :
    D = B**2 - 4*A*C  
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0 

def solve_equation(A,B,C) -> int:
    if A == 0 :
        return linear(B -B ,C)
    else:
        return squarer(A,B,C)

#A,B,C = int(input()), int(input()), int(input())
#print(solve_equation(A,B,C))

    