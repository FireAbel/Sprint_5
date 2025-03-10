from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


def test_successful_registration_redirect_to_main_page(driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('alekseevnikita15.001@yandex.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('htedcxa')
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_invalid_password_registration_viewed_error(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*Locators.REGISTER_NAME_INPUT).send_keys('Тест')
    driver.find_element(*Locators.REGISTER_EMAIL_INPUT).send_keys('alekseevnikita15.021@yandex.ru')
    driver.find_element(*Locators.REGISTER_PASSWORD_INPUT).send_keys('123')  # Некорректный пароль (меньше 6 символов)
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
    error_message = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTER_ERROR_MESSAGE))

    assert error_message.is_displayed()
    assert error_message.text == 'Некорректный пароль'
