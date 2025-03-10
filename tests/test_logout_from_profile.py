from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


def test_logout(driver, login):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
