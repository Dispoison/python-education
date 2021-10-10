"""Module with my copy of range embedded function"""


def my_range(start=0, end=None, step=1):
    """My copy of range embedded function"""
    if step == 0:
        raise ValueError('step must not be zero')
    if end is None:
        end = start
        start = 0
    condition = start < end if step > 0 else start > end
    while condition:
        yield start
        start += step
        condition = start < end if step > 0 else start > end


def main():
    """Main function of generator module"""
    for i in my_range(3):
        print(i, end=' ')
    print()

    for i in my_range(1, 3):
        print(i, end=' ')
    print()

    for i in my_range(2, 6, 2):
        print(i, end=' ')
    print()

    for i in my_range(7, 1, -2):
        print(i, end=' ')
    print()

    for i in my_range(1, 2, 0):
        print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
