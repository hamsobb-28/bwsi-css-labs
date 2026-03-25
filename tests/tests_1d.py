"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]        # Test for positive numbers
    assert two_sum([3, 2, 4], 6) == [1, 2]             # Test for positive numbers
    assert two_sum([3, 3], 6) == [0, 1]                # Test for duplicate numbers
def test_two_sum_edge_cases():
    assert two_sum([1, 2, 3, 4, 5], 5) == [1, 2]          # Test for numbers at the ends of the list
    assert two_sum([-1, -2, -3, -4], -5) == [1, 2]   # Test for negative numbers
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]        # Test for zeros in the list
    assert two_sum([1, 2], 3) == [0, 1]              # Test for a simple case with two numbers

if __name__ == "__main__":
    pytest.main()