import sys
import pytest
def test_f1():
    x=10
    y=20
    assert x==y,"Values are not equal"
@pytest.mark.skipif(sys.version_info<(3,12),reason="version is below 3.12")
def test_f2():
    str1="wipro"
    str2="Welcome to wipro for training session"
    assert str1 in str2
