"""Unit tests of algorithms_practice module"""


import random
import pytest

from ..recursive_factorial import factorial, NegativeValueError
from ..binary_search import binary_search
from ..quick_sort_iterative import quick_sorted_list


def quick_sort_data():
    """Generates random data for quick sort test"""
    def generate_data(times, start, end, count):
        list_of_tuples = []
        for _ in range(times):
            rand_list = random.sample(range(start, end), count)
            sorted_list = sorted(rand_list)
            list_of_tuples.append((rand_list, sorted_list))
        return list_of_tuples

    parametrize_list = []
    parametrize_list.extend(generate_data(5, -2, 2, 3))
    parametrize_list.extend(generate_data(5, -100, 100, 30))
    parametrize_list.extend(generate_data(3, -1000000, 1000000, 100000))

    return parametrize_list


def binary_search_data():
    """Generates random data for binary search test"""
    def generate_data(times, start, end, count):
        list_of_tuples = []
        for _ in range(times):
            sorted_random_list = sorted(random.sample(range(start, end), count))
            index = random.randint(0, count-1)
            number = sorted_random_list[index]

            list_of_tuples.append((sorted_random_list, number, index))
        return list_of_tuples

    parametrize_list = []
    parametrize_list.extend(generate_data(5, -2, 2, 3))
    parametrize_list.extend(generate_data(5, -100, 100, 30))
    parametrize_list.extend(generate_data(3, -1000000, 1000000, 100000))

    return parametrize_list


@pytest.mark.parametrize('number, expected', [(0, 1),
                                              (1, 1),
                                              (2, 2),
                                              (3, 6),
                                              (4, 24),
                                              (5, 120),
                                              (25, 15511210043330985984000000)])
def test_recursive_factorial(number, expected):
    """Verify factorial function"""
    assert factorial(number) == expected


@pytest.mark.parametrize('argument, exception', [('6', TypeError),
                                                 (-1, NegativeValueError)])
def test_recursive_factorial_exceptions(argument, exception):
    """Verify exception handling"""
    with pytest.raises(exception):
        factorial(argument)


@pytest.mark.parametrize('random_list, sorted_list', quick_sort_data())
def test_quick_sort(random_list, sorted_list):
    """Verify quick_sort function on random data"""
    assert quick_sorted_list(random_list) == sorted_list


@pytest.mark.parametrize('sorted_random_list, number, index', binary_search_data())
def test_binary_search(sorted_random_list, number, index):
    """Verify binary_search function on random data"""
    assert binary_search(sorted_random_list, number) == index
