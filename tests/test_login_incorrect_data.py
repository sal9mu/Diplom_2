import pytest
import allure
import requests
import generators
from URL import URL
from data import Response


class TestIncorrectLoginData():

    @allure.title('Проверка авторизации без логина. Ручка Ручка /api/auth/login')
    def test_login_without_email(self, create_user):
        with allure.step('Создаем данные для логина без email'):
            login_data = {'email': '', 'password': create_user[3]}
        with allure.step('Делаем запрос на логин пользователя'):
            response = requests.post(f'{URL.MAIN_URL}{URL.LOGIN_USER}', json = login_data)
        with allure.step('Проверка появления ошибки'):
            assert response.status_code == 401 and (response.json() == Response.unsuccessful_login)

    @allure.title('Проверка авторизации без пароля. Ручка Ручка /api/auth/login')
    def test_login_without_password(self, create_user):
        with allure.step('Создаем данные для логина без пароля'):
            login_data = {'email': create_user[2], 'password': ''}
        with allure.step('Делаем запрос на логин пользователя'):
            response = requests.post(f'{URL.MAIN_URL}{URL.LOGIN_USER}', json = login_data)
        with allure.step('Проверка появления ошибки'):
            assert response.status_code == 401 and (response.json() == Response.unsuccessful_login)
