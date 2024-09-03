from selenium.webdriver.common.by import By

class Locators:
    # Локаторы для страницы регистрации
    NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')  # Поле ввода имени
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')  # Поле ввода email
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка регистрации
    INPUT_ERROR = (By.XPATH, '//div[@class="input__error text_type_main-default"]')  # Сообщение об ошибке регистрации

    # Локаторы для страницы входа
    LOGIN_BUTTON_MAIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_PERSONAL = (By.XPATH, '//p[text()="Личный кабинет"]/..')  # Кнопка "Личный кабинет"
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # Кнопка входа на странице логина

    # Локаторы для перехода в личный кабинет и обратно
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')  # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, '//div[contains(@class, "AppHeader_header__logo")]')  # Логотип Stellar Burgers

    # Локатор для выхода из аккаунта
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выйти"]')  # Кнопка "Выйти" в личном кабинете

    # Локаторы для разделов конструктора
    BUNS_SECTION = (By.XPATH, '//span[text()="Булки"]')  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]')  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]')  # Раздел "Начинки"

    # Основные ссылки для проверок
    BASE_URL = 'https://stellarburgers.nomoreparties.site'  # Главная страница
    LOGIN_URL = 'https://stellarburgers.nomoreparties.site/login'  # Страница логина
    CONSTRUCTOR_URL = 'https://stellarburgers.nomoreparties.site/constructor'  # Страница конструктора
    PROFILE_URL = 'https://stellarburgers.nomoreparties.site/profile'  # Страница профиля
