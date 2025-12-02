from algorithms.recursive_funcs.factorial import calculateFactorial


def test_factorial_of_one():
    assert calculateFactorial(1) == 1

def test_factorial_of_0():
    assert calculateFactorial(0) == 1

def test_factorial_of_5():
    assert calculateFactorial(5) == 120
