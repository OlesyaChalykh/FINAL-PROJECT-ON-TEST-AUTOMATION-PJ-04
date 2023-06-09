import pytest
from pages.auth import *
from pages.settings import *
import time

'''TRK-017 Негативный сценарий регистрации на сайте, невалидный формат Имя.
 Использование тестирования анализа классов эквивалентности и XSS инъекции'''
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('firstname', ['', generate_string_rus(1), generate_string_rus(31),
                                       generate_string_rus(256), english_chars(),
                                       special_chars(), 78489, alternative_keyboard(),japanese_hieroglyph(),
                                       chinese_character(),safety_XSS(),XSS_admixture_HTML()],
                         ids=['TRK-017-1) empty line', 'TRK-017-2) one char', 'TRK-017-3) 31 chars', 'TRK-017-4) 256 chars', 'TRK-017-5) english',
                              'TRK-017-6) special', 'TRK-017-7) number', 'TRK-017-8) alternative_keyboard', 'TRK-017-9) japanese_hieroglyph',
                              'TRK-017-10) chinese_character','TRK-017-11) safety_XSS','TRK-017-12) XSS_admixture_HTML'])

def test_get_registration_invalid_format_firstname(browser, firstname):
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(firstname)
    browser.implicitly_wait(2)
    # Вводим фамилию:
    page.enter_lastname(fake_lastname)
    browser.implicitly_wait(2)
    # Вводим адрес почты/Email:
    page.enter_email(fake_email)
    browser.implicitly_wait(2)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(2)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(2)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print('Необходимо заполнить поле кириллицей. От 2 до 30 символов.')


'''TRK-018 Негативный сценарий регистрации на сайте, невалидный формат Фамилия.
Использование тестирования анализа классов эквивалентности и XSS инъекции'''
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('lastname', ['', generate_string_rus(1), generate_string_rus(31),
                                       generate_string_rus(256), english_chars(),
                                       special_chars(), 78489, alternative_keyboard(),japanese_hieroglyph(),
                                       chinese_character(),safety_XSS(),XSS_admixture_HTML()],
                         ids=['TRK-018-1) empty line', 'TRK-018-1) one char', 'TRK-018-3) 31 chars', 'TRK-018-4) 256 chars', 'TRK-018-5) english',
                              'TRK-018-6) special', 'TRK-018-7) number', 'TRK-018-8) alternative_keyboard', 'TRK-018-9) japanese_hieroglyph',
                              'TRK-018-10) chinese_character','TRK-018-11) safety_XSS','TRK-018-12) XSS_admixture_HTML'])

def test_get_registration_invalid_format_lastname(browser, lastname):

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(fake_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(fake_email)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print('Необходимо заполнить поле кириллицей. От 2 до 30 символов.')


'''TRK-019 Проверка Регистрации на странице, невалидный формат номера Телефона.
Использование тестирования анализа классов эквивалентности'''
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('phone', ['', 7, 7777777777, generate_string_rus(11), english_chars(),special_chars()],
                         ids=['TRK-019-1) empty line', 'TRK-019-2) one digit', 'TRK-019-3) 10_digits', 'TRK-019-4) string_rus', 'TRK-019-5) english_chars',
                              'TRK-019-6) special_chars'])
def test_get_registration_invalid_format_phone(browser, phone):
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(fake_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(fake_lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты/E-mail:
    page.enter_email(phone)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                              'или email в формате example@email.ru'
    print('Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' 
                              '\nили email в формате example@email.ru')


'''TRK-020 Проверка Регистрации на странице, невалидный формат E-mail'''
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('email', ['', '@', '@.', '.', generate_string_rus(20), f'{russian_chars()}@mail.ru',
                                    77777],
                         ids=['TRK-020-1) empty line', 'TRK-020-2) at', 'TRK-020-3) at point', 'TRK-020-4) point', 'TRK-020-5) string', 'TRK-020-6) russian',
                               'TRK-020-7) digits'])
def test_get_registration_invalid_format_email(browser, email):
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(fake_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(fake_lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты/E-mail:
    page.enter_email(email)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                              'или email в формате example@email.ru'
    print('Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' 
                              '\nили email в формате example@email.ru')

'''TRK-021 Проверка, Регистрация в системе: существующий аккаунт по E-mail'''
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('address', [ valid_email],
                         ids=['living email'])
def test_get_registration_living_account(browser, address):
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(fake_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(fake_lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(address)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()
    time.sleep(2)
    card_modal_title = browser.find_element(*RegLocators.REG_CARD_MODAL)

    assert card_modal_title.text == 'Учётная запись уже существует'
    print('TRK-021 Учётная запись уже существует')

'''TRK-022 Проверка, Регистрация в системе: поле пароль и подтверждение пароля не совпадают'''
@pytest.mark.reg
@pytest.mark.negatvie
def test_get_registration_diff_pass_and_pass_conf(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(fake_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(fake_lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(fake_email)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(valid_pass_reg)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()
    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    time.sleep(5)
    assert error_mess.text == 'Пароли не совпадают'
    print('TRK-022 Пароли не совпадают')