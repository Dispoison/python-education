"""Two examples of context manager class"""

import time
import tracemalloc

from generator import my_range


class UsedMemory:
    """Context manager class to check used memory value"""
    def __init__(self):
        self.current = None
        self.peak = None

    def __enter__(self):
        tracemalloc.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.current, self.peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f'Memory usage: {self.current / 1000000} MB')
        print(f'Peak usage: {self.peak / 1000000} MB')
        if exc_val:
            raise exc_val


class ElapsedTime:
    """Context manager class to check elapsed time value"""
    def __init__(self):
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f'Elapsed time: {self.end - self.start} seconds')
        if exc_val:
            raise exc_val


def main():
    """Main function of context_manager module"""
    with UsedMemory(), ElapsedTime():
        _ = list(my_range(1000000))


if __name__ == '__main__':
    main()
