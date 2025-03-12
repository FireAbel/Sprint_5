from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON_MAIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка "Войти в аккаунт" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]')  # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  # Логотип Stellar Burgers

    REGISTER_NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')  # Поле ввода имени
    REGISTER_EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле ввода email
    REGISTER_PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # Поле ввода пароля
    REGISTER_SUBMIT_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка "Зарегистрироваться"
    REGISTER_LOGIN_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj"]') # Кнопка "Войти"
    REGISTER_ERROR_MESSAGE = (By.XPATH, '//p[text()="Некорректный пароль"]')  # Ошибка при регистрации
    FORGOT_LOGIN_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj"]') #Кнопка "Войти" на странице "Забыли пароль"

    LOGIN_EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле ввода email на странице входа
    LOGIN_PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # Поле ввода пароля
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # Кнопка "Войти"

    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  # Кнопка "Выход" из аккаунта

    BUNS_ACTIVE_TAB = (By.XPATH, '//div[contains(@class, "tab_tab_type_current") and span[text()="Булки"]]') # Активная кнопка секции "Булки"
    SAUCES_ACTIVE_TAB = (By.XPATH, '//div[contains(@class, "tab_tab_type_current") and span[text()="Соусы"]]') # Активная кнопка секции "Соусы"
    FILLINGS_ACTIVE_TAB = (By.XPATH, '//div[contains(@class, "tab_tab_type_current") and span[text()="Начинки"]]') # Активная кнопка секции "Начинки"

    BUNS_SECTION_BUTTON = (By.XPATH, '//span[text()="Булки"]/parent::div') # Кнопка секции "Булки"
    SAUCES_SECTION_BUTTON = (By.XPATH, '//span[text()="Соусы"]/parent::div') # Кнопка секции "Соусы"
    FILLINGS_SECTION_BUTTON = (By.XPATH, '//span[text()="Начинки"]/parent::div') # Кнопка секции "Начинки"
