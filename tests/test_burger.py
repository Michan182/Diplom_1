from unittest.mock import patch
import pytest
from unittest.mock import Mock
from Praktikum.burger import Burger
from unittest.mock import call


class TestBurger:
    burger = Burger()
    mock_1 = Mock()
    mock_2 = Mock()
    test_data = {
        'bun_name': {
            'eng': 'Bulka',
            'rus': 'Булка',
            'int': 666
        },
        'sauce_name': {
            'eng': 'Sauce',
            'rus': 'Соус',
            'int': 777,
        },
        'type': {
            'eng': 'Spicy',
            'rus': 'Острый',
            'int': 777,

        },
        'price': {
            'float': 66.66,
            'int': 66,
            'zero_float': 0,
            'zero_int': 0.0
        }
    }

    def test_set_buns_success(self):

        burger = Burger()
        burger.set_buns(self.mock_1)

        assert burger.bun == self.mock_1

    def test_add_ingredient_success(self):

        burger = Burger()
        burger.add_ingredient(self.mock_1)

        assert self.mock_1 in burger.ingredients

    def test_remove_ingredient_success(self):

        burger = Burger()
        burger.add_ingredient(self.mock_1)
        burger.remove_ingredient(0)

        assert self.mock_1 not in burger.ingredients

    def test_move_ingredient_success(self):

        mock_ingredient_1 = self.mock_1
        mock_ingredient_2 = self.mock_1
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[1] == mock_ingredient_1


    @pytest.mark.parametrize('bun_price, ingredient_price, ingredients, expected_result', [
        [test_data['price']['int'], test_data['price']['int'], [mock_2, mock_2], 264],
        [test_data['price']['float'], test_data['price']['float'], [mock_2], 199.98],
        [test_data['price']['int'], test_data['price']['zero_int'], [], 132],
        [test_data['price']['zero_int'], test_data['price']['int'], [mock_2], 66.0],
        [test_data['price']['zero_float'], test_data['price']['zero_float'], [], 0]
    ])
    def test_get_price_success(self, bun_price, ingredient_price, ingredients, expected_result):

        burger = Burger()
        self.mock_1.get_price.return_value = bun_price
        self.mock_2.get_price.return_value = ingredient_price

        with patch.object(burger, 'bun', self.mock_1), \
             patch.object(burger, 'ingredients', ingredients):

            assert burger.get_price() == expected_result


    @pytest.fixture
    def burger_instance(self):
        return Burger()

    def test_get_receipt_success(self):
        burger_instance = Burger()
        bun_object = Mock()
        bun_name = 'Булка'
        ingredient_type = 'начинка'
        ingredient_name = 'ingredient_name'
        ingredients = [Mock(), Mock()]
        price = 666
        expected_result = f'(==== {bun_name} ====)\n= {ingredient_type} {ingredient_name} =\n= {ingredient_type} {ingredient_name} =\n(==== {bun_name} ====)\n\nPrice: {price}'

        burger_instance.bun = bun_object
        burger_instance.ingredients = ingredients
        burger_instance.get_price = Mock(return_value=price)
        bun_object.get_name.return_value = bun_name
        ingredients[0].get_type.return_value = ingredient_type
        ingredients[0].get_name.return_value = ingredient_name
        ingredients[1].get_type.return_value = ingredient_type
        ingredients[1].get_name.return_value = ingredient_name

        assert burger_instance.get_receipt() == expected_result
