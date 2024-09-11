import pytest
from hw2.hw2_debugging import merge_sort
from hw2 import rand

def test_merge_sort_random_array():
    
    test_arr = rand.random_array([None] * 20)
    sorted_arr = merge_sort(test_arr)
    
    assert sorted(test_arr) == sorted_arr
    assert len(sorted_arr) == 20
    assert all(1 <= x <= 20 for x in sorted_arr)
    
