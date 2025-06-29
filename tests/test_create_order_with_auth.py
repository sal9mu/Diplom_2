import pytest
import allure
import requests
from URL import URL
from data import DataForOrder, Flag


class TestCreateOrderWithAuth():

    @allure.title('Проверка создания заказа с авторизацией. Ручка /api/orders')
    @pytest.mark.parametrize('data_for_order', DataForOrder.data_for_order)
    def test_create_order_with_auth(self, create_user, data_for_order):
        with allure.step('Создание пользователя и авторизация'):
            requests.post(f'{URL.MAIN_URL}{URL.LOGIN_USER}', json = create_user[0])

        with allure.step('Создаем данные для заказа'):
            order_data = data_for_order

        with allure.step('Создаем заказ'):
            response = requests.post(f'{URL.MAIN_URL}{URL.CREATE_ORDER}', json = order_data)

        with allure.step('Проверка что заказ создан'):
            assert status_code == 200
            data = response.json()
            for key in Flag.create_order_success:
                assert key in data

