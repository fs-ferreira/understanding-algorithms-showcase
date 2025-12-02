from algorithms.selection_sort.selection_sort import selection_sort

expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

case1 = [10, 5, 2, 6, 8, 1, 3, 7, 9, 4]
case2 = []
case3 = [5]

def test_sort_on_arr():
    assert selection_sort(case1) == expected

def test_sort_on_empty_arr():
    assert selection_sort(case2) == case2
    
def test_sort_on_one_item_arr():
    assert selection_sort(case3) == case3