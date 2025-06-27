import pytest
import allure
import requests
import generators
from URL import URL
from data import Response, IncorrectLogin


class TestIncorrectLoginData():
    @pytest.mark.parametrize('data_for_incorrect_login', IncorrectLogin.incorrect_data)
    @allure.title('Проверка авторизации без логина. Ручка Ручка /api/auth/login')
    def test_login_without_enough_data(self, data_for_incorrect_login):
        with allure.step('Добавляем данные для логина. Без email / без пароля'):
            login_data = data_for_incorrect_login
        with allure.step('Делаем запрос на логин пользователя'):
            response = requests.post(f'{URL.MAIN_URL}{URL.LOGIN_USER}', json = login_data)
        with allure.step('Проверка появления ошибки'):
            assert response.status_code == 401 and (response.json() == Response.unsuccessful_login)

