from Praktikum.bun import Bun
import pytest


class TestBun:

    test_data = {
        'name': {
            'eng': 'Bun',
            'rus': 'Булка',
            'int': 4444
        },
        'price': {
            'float': 3.35,
            'int': 3,
            'zero_float': 0,
            'zero_int': 0.0
        }
    }

    @pytest.mark.parametrize('name', [test_data['name']['rus'], test_data['name']['eng'], test_data['price']['int']])
    def test_get_name_success(self, name):

        bun = Bun(name, 1)

        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [test_data['price']['zero_int'], test_data['price']['zero_float'],
                                       test_data['price']['int'], test_data['price']['float']])
    def test_get_price_success(self, price):

        bun = Bun('Bun', price)

        assert bun.get_price() == price
