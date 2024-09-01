import pytest
from locators import Locators


def test_login_buttons(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Вход по кнопке «Войти в аккаунт» на главной
    driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
    # Ожидание и проверка перехода на страницу после логина
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Вход через кнопку «Личный кабинет»
    driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Вход через кнопку на странице логина
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()
