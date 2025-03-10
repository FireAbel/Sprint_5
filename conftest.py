import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('alekseevnikita15.001@yandex.ru')
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('htedcxa')
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))