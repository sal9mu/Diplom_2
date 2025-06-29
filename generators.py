from faker import Faker

fake = Faker()

def email_generation():
    generation_email = fake.free_email()
    return generation_email

def password_generation():
    generation_password = fake.password()
    return generation_password

def name_generation():
    generation_name = fake.first_name()
    return generation_name
