import pytest
import allure
import requests
from URL import URL
from data import DataForOrder, Response, Flag


class TestCreateOrderWithoutAuth():

    @allure.title('Проверка создания заказа без авторизацией. Ручка /api/orders')
    def test_create_order_without_auth(self):
        with allure.step('Создаем данные для заказа'):
            order_data = DataForOrder.data_for_order[0]

        with allure.step('Создаем заказ'):
            response = requests.post(f'{URL.MAIN_URL}{URL.CREATE_ORDER}', json = order_data)

        with allure.step('Проверка что заказ создан'):
            assert response.status_code == 200
            data = response.json()
            for key in Flag.successful_create_burger:
                assert key in data
