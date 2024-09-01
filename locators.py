from selenium.webdriver.common.by import By

class Locators:
    # Локаторы для страницы регистрации
    NAME_INPUT = (By.NAME, 'name')  # Поле ввода имени
    EMAIL_INPUT = (By.NAME, 'email')  # Поле ввода email
    PASSWORD_INPUT = (By.NAME, 'password')  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка регистрации
    INPUT_ERROR = (By.XPATH, '//div[@class="input__error text_type_main-default"]')  # Сообщение об ошибке регистрации

    # Локаторы для страницы входа
    LOGIN_BUTTON_MAIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_PERSONAL = (By.XPATH, '//a[text()="Личный кабинет"]')  # Кнопка "Личный кабинет"
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # Кнопка входа на странице логина

    # Локаторы для перехода в личный кабинет и обратно
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')  # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  # Логотип Stellar Burgers

    # Локатор для выхода из аккаунта
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выйти"]')  # Кнопка "Выйти" в личном кабинете

    # Локаторы для разделов конструктора
    BUNS_SECTION = (By.XPATH, '//span[text()="Булки"]')  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]')  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]')  # Раздел "Начинки"
