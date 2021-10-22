"""Quick sort iterative module"""


from data_structures_and_algorithms.data_structures_practice.stack import Stack


def _partition_right(numbers, left, right):
    pivot = numbers[right]
    i = left

    for j in range(left, right):
        if numbers[j] <= pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
    numbers[i], numbers[right] = numbers[right], numbers[i]
    return i


def quick_sorted_list(numbers_original):
    """Quick sort iterative method"""
    numbers = numbers_original.copy()
    left = 0
    right = len(numbers) - 1
    stack = Stack()
    stack.push(left)
    stack.push(right)

    while stack.peek():
        right = stack.pop().data
        left = stack.pop().data

        pivot = _partition_right(numbers, left, right)

        if pivot - 1 > left:
            stack.push(left)
            stack.push(pivot - 1)
        if pivot + 1 < right:
            stack.push(pivot + 1)
            stack.push(right)

    return numbers
