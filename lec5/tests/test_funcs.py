import funcs as f 

def test_add():
    assert f.add(2,3) == 5 
    assert f.add(3,3) == 6
    assert f.add(10, -10) == 0
    for i in range(0, 100):
        assert f.add(i, i) == 2*i 

def test_sub():
    assert f.sub(1,2) == -1
    assert f.sub(0,0) == 0
    assert f.sub(10, 9) == 1

def test_mult():
    assert f.mult(10, 20) == 200
    assert f.mult(2, 3) == 6