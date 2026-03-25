"""
tests_1c.py

This module contains unit tests for the simple_calculator function defined in lab_1c.py
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([0,1,2,3,-1]) == 6 # Test for a simple case with positive numbers
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6 # Test for a case with both positive and negative numbers
    assert max_subarray_sum([-1]) == -1 # Test for a single negative number
    assert max_subarray_sum([-2,-3,-1]) == -1 # Test for all negative numbers
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23 # Test for a case where the maximum subarray includes the end of the list
    assert max_subarray_sum([0, -2, 3, 5, -1, 2]) == 9 # Test for a case where the maximum subarray is in the middle of the list

def test_max_subarray_sum_edge_cases():
    assert max_subarray_sum([0]) == 0 # Test for a single zero
    assert max_subarray_sum([-1, -2, -3, -4]) == -1 # Test for all negative numbers with the maximum being the least negative
    assert max_subarray_sum([1, 2, 3, 4]) == 10 # Test for all positive numbers
    assert max_subarray_sum([0, 0, 0, 0]) == 0 # Test for all zeros
    assert max_subarray_sum([1, -1, 1, -1, 1]) == 1 # Test for alternating positive and negative numbers

if __name__ == "__main__":
    pytest.main()