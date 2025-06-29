import pytest
import allure
import requests
from URL import URL
from data import Flag, Response


class TestCreateBurgerWithIngrefients():

    @allure.title('Проверка создания бургера без начинки. Ручка /api/orders')
    def test_create_order_with_ingredients(self):
        with allure.step('Создаем данные для заказа'):
            order_data = {}

        with allure.step('Создаем заказ'):
            response = requests.post(f'{URL.MAIN_URL}{URL.CREATE_ORDER}', json = order_data)

        with allure.step('Проверка что заказ создан'):
            assert response.status_code == 400 and (response.json() == Response.without_ingredients)