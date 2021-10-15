"""Module with FibonacciContainer and FibonacciIterator"""


class NonPositiveIntegerValueError(ValueError):
    """Exception if the value is not a positive integer"""


class FibonacciContainer:
    """Fibonacci iterator container"""
    def __init__(self, number: int):
        self._number = number
        self.validate_number(self._number)

    def __iter__(self):
        return FibonacciIterator(self._number)

    def __str__(self):
        return f'{self._number}\'th number fibonacci: {self.numbers()[-1]}'

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.numbers()[key]
        if isinstance(key, slice):
            return ' '.join(self.numbers()[key])
        raise TypeError

    def numbers(self, number=None):
        """Returns list of <number> fibonacci numbers"""
        if number is None:
            number = self._number
        return list(FibonacciIterator(number))

    @staticmethod
    def validate_number(number):
        """Checks if the value of a number is correct"""
        if not number > 0:
            raise NonPositiveIntegerValueError('number must be positive integer number')


class FibonacciIterator:
    """Fibonacci iterator"""
    def __init__(self, number):
        self._counter = 0
        self._first_number = 1
        self.next_number = 1
        self._number = number

    def get_number(self):
        """Get next fibonacci number"""
        self._counter += 1
        if self._counter > self._number:
            raise StopIteration
        if self._counter == 1 or self._counter == 2:
            return self._first_number
        first_number = self._first_number
        self._first_number += self.next_number
        self.next_number = first_number
        return self._first_number

    def __next__(self):
        return self.get_number()

    def __iter__(self):
        return self


def main():
    """Main function of iterator module"""
    fibonacci = FibonacciContainer(10)
    for fib in fibonacci:
        print(fib)

    print(FibonacciContainer(8))


if __name__ == '__main__':
    main()
