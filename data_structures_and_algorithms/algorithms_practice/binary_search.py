"""Binary search module"""


def _run_recursive(numbers, target, left, right):
    middle = (right + left) // 2

    if numbers[left] == numbers[right] != target:
        return -1

    if numbers[middle] > target:
        return _run_recursive(numbers, target, left, middle - 1)
    if numbers[middle] < target:
        return _run_recursive(numbers, target, middle + 1, right)
    return middle


def binary_search(numbers, target):
    """Method find returns value index"""
    return _run_recursive(numbers, target, 0, len(numbers) - 1)
