import pytest
import requests
import generators
from URL import URL


@pytest.fixture
def create_user():
    email = generators.email_generation()
    password = generators.password_generation()
    name = generators.name_generation()
    create_user_body = {'email': email, 'password': password, "name": name}
    login_user_body = {'email' : email, 'password' : password}
    requests.post(f'{URL.MAIN_URL}{URL.CREATE_USER}', json = create_user_body)
    login_user = requests.post(f'{URL.MAIN_URL}{URL.LOGIN_USER}', json = login_user_body)
    yield [create_user_body, login_user_body, email, password]
    requests.delete(f'{URL.MAIN_URL}{URL.DELETE_USER}{login_user.json()}')

@pytest.fixture
def generate_user_data():
    email = generators.email_generation()
    password = generators.password_generation()
    name = generators.name_generation()
    create_user_body = {'email': email, 'password': password, "name": name}
    login_user_body = {'email': email, 'password': password}
    yield [create_user_body, login_user_body]
    login_user = requests.post(f'{URL.MAIN_URL}{URL.LOGIN_USER}', json = login_user_body)
    requests.delete(f'{URL.MAIN_URL}{URL.DELETE_USER}{login_user.json()}')
