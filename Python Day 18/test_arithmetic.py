import pytest
from arithmetic import*
def test_add():
    assert add(10,20)==30
    assert add(-19,-20)==-39
    assert add(-20,10)==-10
def test_sub():
    assert sub(-2,-1)==1
    assert sub(10,-20)==30
    assert sub(-20,10)==-30
def test_power():
    assert power(2,3)==8
    assert power(-2,4)==16
    assert power(3,4)==81