"""Example of restaurant work cycle."""

import datetime
import argparse

from restaurant import Menu
from restaurant import Dish
from restaurant import Cook
from restaurant import Waiter
from restaurant import Administrator
from restaurant import Courier
from restaurant import InternetService
from restaurant import LocalCustomer
from restaurant import RemoteCustomer


def example(order_type):
    """Makes example data and runs it."""
    menu = Menu()
    Dish('borsch', 'soup', 100, 400)
    Dish('pelmeni', 'meat', 80, 300)
    Dish('kartoshka', 'garnir', 60, 250)

    Cook('Oleg', 'Efremov', '+380971234567', 'oleg@gmail.com',
         'm', datetime.date(1990, 4, 13), 'Kharkiv', 115253576)

    waiter = Waiter('Vitalii', 'Maliarenko', '+380971234567', 'vitalii@gmail.com',
                    'm', datetime.date(1990, 4, 13), 'Kharkiv', 115253576)

    Administrator('Vlad', 'Ivanov', '+380971234567', 'vlad@gmail.com',
                  'm', datetime.date(1990, 4, 13), 'Kharkiv', 115253576)

    courier = Courier('Vlad', 'Ivanov', '+380971234567', 'vlad@gmail.com',
                      'm', datetime.date(1990, 4, 13), 'Kharkiv', 115253576)

    internet_service = InternetService(menu)

    local_customer = LocalCustomer('Petro')
    remote_customer = RemoteCustomer('Vasya', 'Klochkovskaya 55', '+380972336567')

    if order_type == 'local':
        waiter.service(local_customer, menu)
    elif order_type == 'remote':
        remote_customer.use_internet_service(internet_service)
    else:
        local_customer.make_comment(f'Very bad service from {waiter}')
        remote_customer.make_comment(f'Very long delivery from {courier}')
        print(local_customer.get_all_comments())
        print(remote_customer.get_all_comments())


def main():
    """Main function of example file."""
    parser = argparse.ArgumentParser(description='Order type')
    parser.add_argument('-t', '--type', type=str, default=None, required=False,
                        help='"local" or "remote" order')

    args = parser.parse_args()
    order_type = args.type

    example(order_type)


if __name__ == '__main__':
    main()
