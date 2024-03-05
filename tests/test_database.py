from Praktikum.database import Database
from Praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest

@pytest.fixture
def database_instance():
    return Database()

def test_available_buns(database_instance):
    buns = database_instance.available_buns()
    assert len(buns) == 3  # Проверяем, что список доступных булок содержит три элемента

def test_available_ingredients(database_instance):
    ingredients = database_instance.available_ingredients()
    assert len(ingredients) == 6  # Проверяем, что список доступных ингредиентов содержит шесть элементов

    # Проверяем, что все ингредиенты имеют правильный тип
    for ingredient in ingredients:
        assert ingredient.get_type() in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]

# Дополнительные тесты можно добавить для проверки других методов класса Database, если они есть.
