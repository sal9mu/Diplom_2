import pytest
import allure
import requests
from URL import URL
from data import Flag, DataForOrder


class TestCreateBurgerWithIngrefients():

    @allure.title('Проверка создания бургера с начинкой. Ручка /api/orders')
    def test_create_order_with_ingredients(self):
        with allure.step('Создаем данные для заказа'):
            order_data = DataForOrder.data_for_order[0]

        with allure.step('Создаем заказ'):
            response = requests.post(f'{URL.MAIN_URL}{URL.CREATE_ORDER}', json = order_data)

        with allure.step('Проверка что заказ создан'):
            data = response.json()
            for key in Flag.successful_create_burger:
                assert key in data
