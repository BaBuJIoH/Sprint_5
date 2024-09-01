import pytest
from locators import Locators

def test_successful_registration(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*Locators.NAME_INPUT).send_keys('Aleksandr')
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('aleksandr_kurbakov_13_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('Qweasd!23')
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    # Проверка успешной регистрации
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/constructor'
    driver.quit()

def test_registration_error_for_invalid_password(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*Locators.NAME_INPUT).send_keys('Aleksandr')
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('aleksandr_kurbakov_13_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('qwe')
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    error_message = driver.find_element(*Locators.INPUT_ERROR).text

    # Проверка неудачной регистрации
    assert 'Некорректный пароль' in error_message
    driver.quit()
