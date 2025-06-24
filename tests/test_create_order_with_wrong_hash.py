import pytest
import allure
import requests
from URL import URL
from data import DataForOrder, Response, Flag


class TestCreateOrderWithWrongHash():

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов. Ручка /api/orders')
    def test_create_order_with_wrong_hash(self):
        with allure.step('Создаем данные для заказа'):
            order_data = {"ingredients": '00000000000000000000000'}

        with allure.step('Создаем заказ'):
            response = requests.post(f'{URL.MAIN_URL}{URL.CREATE_ORDER}', json = order_data)

        with allure.step('Проверка получения ошибка'):
            assert response.status_code == 500
