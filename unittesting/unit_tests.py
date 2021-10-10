"""Unit tests for code in module to_test.py."""

import pytest

from to_test import even_odd
from to_test import sum_all
from to_test import time_of_day
from to_test import Product
from to_test import Shop


@pytest.mark.parametrize('value, expected', [(1, 'odd'),
                                             (8, 'even'),
                                             (0, 'even'),
                                             (-11, 'odd')])
def test_even_odd(value, expected):
    """Verifies even_odd function that the parity of a number is correctly determined."""
    assert even_odd(value) == expected


@pytest.mark.parametrize('value', [('7',),
                                   (1.5,)])
def test_even_odd_wrong_input_type_error(value):
    """Verifies even_odd function behavior when entering data of the wrong type."""
    with pytest.raises(TypeError):
        even_odd(value)


@pytest.mark.parametrize('numbers, expected', [((1, 2, 3, 4, 5, 6), 21),
                                               ((4, 2, 0, 3, 0, -10), -1),
                                               ((1, 0.5), 1.5),
                                               ((0,), 0)])
def test_sum_all(numbers, expected):
    """Verifies if the sum of the given numbers is correct."""
    assert sum_all(*numbers) == expected


@pytest.mark.parametrize('datetime_, expected', [('2021-10-08 05:00:00', 'night'),
                                                 ('2021-10-08 11:00:00', 'morning'),
                                                 ('2021-10-08 17:00:00', 'afternoon'),
                                                 ('2021-10-08 22:00:00', 'night')])
def test_time_of_day(freezer, datetime_, expected):
    """Verifies the function time_of_day to determine the correct time of day."""
    freezer.move_to(datetime_)
    assert time_of_day() == expected


@pytest.fixture(name='product')
def product_object():
    """Creates first product object example."""
    return Product(title='Juice', price=34, quantity=15)


@pytest.fixture(name='product2')
def product2_object():
    """Creates second product object example."""
    return Product(title='coca-cola', price=29, quantity=11)


class TestProduct:
    """Contains tests to verify Product functionality."""
    @staticmethod
    @pytest.mark.parametrize('value, expected', [(1, 14),
                                                 (5, 10),
                                                 (15, 0)])
    def test_product_subtract(product, value, expected):
        """Verifies the subtract_quantity function to determine
        if the subtracted quantity of the product is correct."""
        product.subtract_quantity(value)
        assert product.quantity == expected

    @staticmethod
    @pytest.mark.parametrize('value, expected', [(0, 15),
                                                 (5, 20),
                                                 (7, 22)])
    def test_product_add(product, value, expected):
        """Verifies the add_quantity function to determine
        if the added quantity of the product is correct."""
        product.add_quantity(value)
        assert product.quantity == expected

    @staticmethod
    @pytest.mark.parametrize('value, expected', [(1, 1),
                                                 (7, 7),
                                                 (35, 35)])
    def test_product_change_price(product, value, expected):
        """Verifies the change_price function to determine
        if the changed price of the product is correct."""
        product.change_price(value)
        assert product.price == expected


class TestShop:
    """Contains tests to verify Shop functionality."""

    @staticmethod
    def get_product_index(products, product_title):
        """Returns index of product in list with specified title if exists."""
        for index, product in enumerate(products):
            if product.title == product_title:
                return index
        return None

    @staticmethod
    @pytest.fixture(name='init_no_args')
    def creation_no_arg():
        """Creates shop without products in constructor."""
        return Shop()

    @staticmethod
    @pytest.fixture(name='init_with_a_product')
    def creation_one_product_arg(product):
        """Creates shop with a product in constructor."""
        return Shop(product)

    @staticmethod
    @pytest.fixture(name='init_with_a_list')
    def creation_list_arg(product, product2):
        """Creates shop with a list of products in constructor."""
        return Shop([product, product2])

    @staticmethod
    def test_creation_no_arg(init_no_args):
        """Verifies correct value of products attribute
        after creating shop without any arguments."""
        assert init_no_args.products == []

    @staticmethod
    def test_creation_one_product_arg(init_with_a_product, product):
        """Verifies correct value of products attribute
         after creating shop with a product."""
        assert init_with_a_product.products == [product]

    @staticmethod
    def test_creation_list_arg(init_with_a_list, product, product2):
        """Verifies correct value of products attribute
        after creating shop with list of products."""
        assert init_with_a_list.products == [product, product2]

    @staticmethod
    def test_add_product(init_no_args, product):
        """Verifies correct value of products attribute after adding new product."""
        init_no_args.add_product(product)
        assert init_no_args.products == [product]

    @staticmethod
    @pytest.mark.parametrize('quantity, expected', [(5, 10),
                                                    (1, 14)])
    def test_sell_product(init_with_a_product, product, quantity, expected):
        """Verifies correct value of product quantity after selling it
           when the quantity is less than the existing quantity."""
        init_with_a_product.sell_product(product.title, quantity)
        products = init_with_a_product.products
        product_index = TestShop.get_product_index(products, product.title)
        product = init_with_a_product.products[product_index]
        assert product.quantity == expected

    @staticmethod
    def test_sell_product_full_sale(init_with_a_product, product):
        """Verifies deleting of product after selling it
           when the quantity is equals the existing quantity."""
        init_with_a_product.sell_product(product.title, product.quantity)
        products = init_with_a_product.products
        product_index = TestShop.get_product_index(products, product.title)
        assert product_index is None

    @staticmethod
    def test_sell_product_over_quantity_error(init_with_a_product, product):
        """Verifies sell_product function behavior when input quantity greater than existing."""
        with pytest.raises(ValueError):
            init_with_a_product.sell_product(product.title, product.quantity + 1)
