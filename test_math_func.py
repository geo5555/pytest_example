import math_func
import pytest

def test_add():
    assert math_func.add(7, 3) == 10
    result = math_func.add('hello', 'world')
    assert result == 'helloworld'
    assert type(result) is str
    assert 'helo' not in result
    result = math_func.add(10.5,25.5)
    assert result == 36
    
