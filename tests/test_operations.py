from src.math_operations import add,sub,multi

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1
    
def test_multi():
    assert multi(2,3)==6
    assert multi(4,5)==20
    assert multi(-1,-2)==2