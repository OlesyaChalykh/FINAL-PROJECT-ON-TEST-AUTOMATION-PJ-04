from faker import Faker
import string

'''Фейковые данные для авторизации в системе'''
fake_ru = Faker('ru_RU')#параметры с русским алфавитом
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
fake = Faker()#параметры с ангилийским алфавитом
fake_password = fake.password()
fake_email = fake.email()
fake_login = fake.user_name()

invalid_ls = '1234567890'


valid_firstname_reg = 'Маша'
valid_lastname_reg = 'Васина'
valid_email = 'giiip33u2m@wuuvo.com'
valid_pass_reg = 'Qq123456789!'

def generate_string_rus(n):
    return 'я' * n

def generate_string_en(n):
    return 's' * n

def english_chars():
    return 'qwertyuiopasdfghjkl'

def russian_chars():
    return 'йцукенгшщзхъфывапролджэ'

def special_chars():
    return f'{string.punctuation}' #Специальные симовлы

def alternative_keyboard():
    return '!@#$%^&*()'
def japanese_hieroglyph():#Японские иероглифы
    return   '原千五百秋瑞'
def chinese_character():# Китайсике иероглифы
    return   '龍門大酒家'
def XSS_admixture_HTML(): #Тестирование на безопасность XSS примесь HTML
    return '<IMG src="#">'
def safety_XSS(): #Тестирование на безопасность XSS инъекция
    return '<script>alert("Поле input уязвимо!")</script>|'