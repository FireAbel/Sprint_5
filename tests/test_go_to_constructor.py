from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


def test_constructor_navigation(driver, login):
    driver.get('https://stellarburgers.nomoreparties.site/account')

    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_go_to_constructor_from_logo(driver, login):
    driver.get('https://stellarburgers.nomoreparties.site/account')

    driver.find_element(*Locators.LOGO_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'