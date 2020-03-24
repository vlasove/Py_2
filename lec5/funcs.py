def add(a:int, b:int) -> int:
    return a + b 

def sub(a:int, b:int) -> int:
    return a -b 

def mult(a:int, b:int) -> int:
    return a * b 

def div(a:int, b:int) -> int:
    return a // b 


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(div(a,b))

python -m pytest tests/test_funcs.py