from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


def test_login_from_account_button(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('alekseevnikita15.001@yandex.ru')
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('htedcxa')
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_login_from_button_login(driver):
    driver.get('https://stellarburgers.nomoreparties.site')

    driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('alekseevnikita15.001@yandex.ru')
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('htedcxa')
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_login_from_button_on_registration_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*Locators.REGISTER_LOGIN_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('alekseevnikita15.001@yandex.ru')
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('htedcxa')
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_login_from_button_on_forgot_password_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

    driver.find_element(*Locators.FORGOT_LOGIN_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('alekseevnikita15.001@yandex.ru')
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('htedcxa')
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
