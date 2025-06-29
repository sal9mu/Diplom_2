import pytest
import allure
import requests
from URL import URL
from data import Flag


class TestLoginExistUser():

    @allure.title('Проверка успешного входа существующего пользователя. Ручка /api/auth/login')
    def test_login_exist_user(self, create_user):
        with allure.step('Создаем пользователя и входим в аккаунт'):
            response = requests.post(f'{URL.MAIN_URL}{URL.LOGIN_USER}', json = create_user[0])
        with allure.step('Проверка успешного входа'):
            assert response.status_code == 200
            data = response.json()
            for key in Flag.create_user_success:
                assert key in data
