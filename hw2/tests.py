import pytest
from rand import random_array
from hw2_debugging import merge_sort


def test_merge_sort_random_array(): # Test 1: Random Array
    
    test_arr = random_array([None] * 20)
    sorted_arr = merge_sort(test_arr)
    
    assert sorted(test_arr) == sorted_arr
    assert len(sorted_arr) == 20
    assert all(1 <= x <= 20 for x in sorted_arr)
    
def test_merge_sort_ascending_order(): # Test 2: Already Sorted Array
    
    test_arr = list(range(1, 21))  # [1, 2, ..., 20]
    
    sorted_arr = merge_sort(test_arr)
    
    assert sorted_arr == test_arr
    assert len(sorted_arr) == 20

def test_merge_sort_descending_order(): # Test 3: Reverse Sorted Array
    
    test_arr = list(range(20, 0, -1))  # [20, 19, ..., 1]
    
    sorted_arr = merge_sort(test_arr)
    
    assert sorted_arr == list(range(1, 21))
    assert len(sorted_arr) == 20
    