from algorithms.binary_search.binary_search import binary_search

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_found_element():
    assert binary_search(arr, 7) == 6

def test_not_found_element():
    assert binary_search(arr, 11) is None
