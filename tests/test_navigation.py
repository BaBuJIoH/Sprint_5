import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_profile_navigation(driver):
    driver.get(Locators.BASE_URL)

    # Переход в личный кабинет
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PERSONAL)).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Locators.PROFILE_URL))
    assert driver.current_url == Locators.PROFILE_URL

    # Переход в конструктор
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Locators.CONSTRUCTOR_URL))
    assert driver.current_url == Locators.CONSTRUCTOR_URL

    # Переход на главную через логотип
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Locators.BASE_URL))
    assert driver.current_url == Locators.BASE_URL


def test_logout(driver):
    driver.get(Locators.LOGIN_URL)

    # Выполняем вход в систему перед выходом
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(
        'aleksandr_kurbakov_13_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('Qweasd!23')
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Ожидание перехода на страницу профиля
    WebDriverWait(driver, 5).until(EC.url_to_be(Locators.PROFILE_URL))

    # Выход из аккаунта
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Locators.LOGIN_URL))
    assert driver.current_url == Locators.LOGIN_URL
