import pytest
import allure
import requests
import generators
from URL import URL
from data import Response, DataForRegistration


class TestCreateUserWithNoFullData():

    @allure.title('Проверка создания пользователя без одно из обязательных полей. Ручка /api/auth/register')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_create_user_with_no_full_data(self, data_setup):
        with allure.step('Передаем данные без одного обязательного поля'):
            response = requests.post(f'{URL.MAIN_URL}{URL.CREATE_USER}', data_setup)
        with allure.step('Проверка получения ошибки'):
            assert response.status_code == 403 and (response.json() == Response.user_registration_not_enough_data)
