from algorithms.recursive_funcs.factorial import calculateFactorial
from algorithms.recursive_funcs.sum import array_sum
from algorithms.recursive_funcs.array_length import array_len, array_len_v2
from algorithms.recursive_funcs.highest_value import highest


def test_factorial_of_one():
    assert calculateFactorial(1) == 1

def test_factorial_of_0():
    assert calculateFactorial(0) == 1

def test_factorial_of_5():
    assert calculateFactorial(5) == 120

def test_recursive_array_sum_length_4():
    assert array_sum([1,2,3,4]) == 10

def test_recursive_array_sum_length_1():
    assert array_sum([4]) == 4

def test_recursive_array_sum_length_0():
    assert array_sum([]) == 0

def test_recursive_array_length_0():
    assert array_len(0, []) == 0

def test_recursive_array_length_1():
    assert array_len(0, [999]) == 1

def test_recursive_array_length_4():
    assert array_len(0, [1,2,3,4]) == 4

def test_recursive_array_length_0_v2():
    assert array_len_v2([]) == 0

def test_recursive_array_length_1_v2():
    assert array_len_v2([999]) == 1

def test_recursive_array_length_4_v2():
    assert array_len_v2([1,2,3,4]) == 4

def test_highest_array_value():
    assert highest([]) == None

def test_highest_array_value_unsorted():
    assert highest([10, 2, 4]) == 10

def test_highest_array_value_sorted():
    assert highest([2, 4, 6, 10]) == 10