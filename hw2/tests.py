# import pytest
"""This module tests the correctness of the merge sort algorithm in hw2_debugging.py"""
from rand import random_array
from hw2_debugging import merge_sort


def test_merge_sort_random_array():  # Test 1: Random Array
    """This test generates a random array and makes sure it is sorted correctly using merge_sort"""
    test_arr = random_array([None] * 20)
    sorted_arr = merge_sort(test_arr)

    assert sorted(test_arr) == sorted_arr
    assert len(sorted_arr) == 20
    assert all(1 <= x <= 20 for x in sorted_arr)


def test_merge_sort_ascending_order():  # Test 2: Already Sorted Array
    """This test asserts that merge_sort works correctly for an already sorted array"""
    test_arr = list(range(1, 21))  # [1, 2, ..., 20]

    sorted_arr = merge_sort(test_arr)

    assert sorted_arr == test_arr
    assert len(sorted_arr) == 20


def test_merge_sort_descending_order():  # Test 3: Reverse Sorted Array
    """This sort asserts that merge_sort works correctly for a reverse sorted array"""
    test_arr = list(range(20, 0, -1))  # [20, 19, ..., 1]

    sorted_arr = merge_sort(test_arr)

    assert sorted_arr == list(range(1, 21))
    assert len(sorted_arr) == 20
