import pytest
import math_func

@pytest.mark.parametrize('num1,num2,result',
                        [(7, 3, 10),
                        ('Hello', 'World', 'HelloWorld'),
                        (10.5, 25.5, 36),
                        (10, 1, 11)
                        ]
                        )
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result
    