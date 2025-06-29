import generators


class DataForRegistration:
    reg_data = [{'password' : generators.password_generation(), 'name' : generators.name_generation()},
                {'email' : generators.email_generation(), 'name' : generators.name_generation()},
                {'name' : generators.name_generation(), 'password' : generators.password_generation()}]

class Response:
    already_exist_user = {"success": False, "message": "User already exists"}
    user_registration_not_enough_data = {"success": False, "message": "Email, password and name are required fields"}
    unsuccessful_login = {"success": False, "message": "email or password are incorrect"}
    without_ingredients = {"success": False, "message": "Ingredient ids must be provided"}
    with_auth = {"success": True}
    without_auth = {"success": False, "message": "You should be authorised"}

class DataForOrder:
    data_for_order = [{"ingredients": ["61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa6c"]},
                      {"ingredients": ["61c0c5a71d1f82001bdaaa73", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6c"]}]

class Flag:
    create_user_success = ('accessToken' , 'refreshToken', 'success')
    create_order_success = ('name', 'order', 'success')
    successful_create_burger = ('name', 'order', 'success')

class InvalidDataForOrder:
    invalid_data = {"ingredients": '00000000000000000000000'}

class IncorrectLogin:
    incorrect_data = [{'email': '', 'password': create_user[3]},
                      {'email': create_user[2], 'password': ''}]
