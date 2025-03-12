from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_go_to_buns_section(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*Locators.FILLINGS_SECTION_BUTTON).click()
    driver.find_element(*Locators.BUNS_SECTION_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.BUNS_ACTIVE_TAB))

    assert driver.find_element(*Locators.BUNS_ACTIVE_TAB).is_displayed()

def test_go_to_sauces_section(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*Locators.SAUCES_SECTION_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.SAUCES_ACTIVE_TAB))

    assert driver.find_element(*Locators.SAUCES_ACTIVE_TAB).is_displayed()

def test_go_to_fillings_section(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*Locators.FILLINGS_SECTION_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.FILLINGS_ACTIVE_TAB))

    assert driver.find_element(*Locators.FILLINGS_ACTIVE_TAB).is_displayed()
