import pytest
import allure
import requests
from URL import URL
from data import Flag


class TestCreateUser():

    @allure.title('Проверка успешного создания уникального пользователя. Ручка /api/auth/register')
    def test_successful_create_user(self, generate_user_data):
        with allure.step('Создаем пользователя'):
            response = requests.post(f'{URL.MAIN_URL}{URL.CREATE_USER}', json = generate_user_data[0])
        with allure.step('Проверка что пользователь успешно создан'):
            assert status_code == 200
            data = response.json()
            for key in Flag.create_user_success:
                assert key in data
