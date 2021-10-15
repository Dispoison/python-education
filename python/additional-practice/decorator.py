"""Module with two decorators to check used memory and elapsed time"""


import tracemalloc
import time

from generator import my_range


def memory_usage(function):
    """Decorator checks used memory value"""
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = function(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(function.__name__)
        print(f'Memory usage: {current / 1000000} MB')
        print(f'Peak usage: {peak / 1000000} MB')
        tracemalloc.stop()
        return result

    return wrapper


def elapsed_time(function):
    """Decorator checks elapsed time value"""
    def wrapper(*args, **kwargs):
        print('-' * 50)
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time: {end - start} seconds')
        print('-' * 50)
        return result

    return wrapper


@elapsed_time
@memory_usage
def list_from_generator(generator, number):
    """Example of decorators usage"""
    return list(generator(number))


def main():
    """Main function of decorator module"""
    list_from_generator(my_range, 10000000)
    print()


if __name__ == '__main__':
    main()
