import random
import string
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


def generate_email():
    base_email = 'alekseevnikita15.'
    unique_part = ''.join(random.choices(string.digits, k=3))
    return f'{base_email}{unique_part}@ya.ru'

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

#Я не заметил, видимо, когда объединял файлы случайно не тот тест вставил сюда
def test_successful_registration_redirect_to_main_page(driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.REGISTER_NAME_INPUT).send_keys('Тест')
        driver.find_element(*Locators.REGISTER_EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*Locators.REGISTER_PASSWORD_INPUT).send_keys(generate_password(7))
        driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_invalid_password_registration_viewed_error(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*Locators.REGISTER_NAME_INPUT).send_keys('Тест')
    driver.find_element(*Locators.REGISTER_EMAIL_INPUT).send_keys('alekseevnikita15.021@yandex.ru')
    driver.find_element(*Locators.REGISTER_PASSWORD_INPUT).send_keys('123')
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
    error_message = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTER_ERROR_MESSAGE))

    assert error_message.is_displayed()
    assert error_message.text == 'Некорректный пароль'
