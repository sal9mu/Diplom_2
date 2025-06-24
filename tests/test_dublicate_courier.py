import pytest
import allure
import requests
import generators
from URL import URL
from data import Response


class TestCreateUserDublicate():

    @allure.title('Проверка создания двух одинаковых пользователей. Ручка /api/auth/register')
    def test_create_duplicate_users(self, create_user):
        with allure.step('Создаем пользователя с уже зарегистрированными данными'):
            response = requests.post(f'{URL.MAIN_URL}{URL.CREATE_USER}', json = create_user[0])
        with allure.step('Проверка получения ошибки'):
            assert response.status_code == 403 and (response.json() == Response.already_exist_user)
