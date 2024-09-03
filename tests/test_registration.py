import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_registration(driver):
    driver.get(Locators.BASE_URL)

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PERSONAL)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()

    driver.find_element(*Locators.NAME_INPUT).send_keys('Aleksandr')
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('aleksandr_kurbakov_13_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('Qweasd!23')
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    # Ожидание URL для проверки успешной регистрации
    WebDriverWait(driver, 5).until(EC.url_to_be(Locators.CONSTRUCTOR_URL))
    assert driver.current_url == Locators.CONSTRUCTOR_URL


def test_registration_error_for_invalid_password(driver):
    driver.get(Locators.BASE_URL)

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PERSONAL)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()

    driver.find_element(*Locators.NAME_INPUT).send_keys('Aleksandr')
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('aleksandr_kurbakov_13_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('qwe')
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    # Ожидание ошибки
    error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_ERROR)).text
    assert 'Некорректный пароль' in error_message
