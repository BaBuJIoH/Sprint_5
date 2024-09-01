import pytest
from locators import Locators


def test_profile_navigation(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/profile'

    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/constructor'

    driver.find_element(*Locators.LOGO_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_logout(login):
    driver = login
    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    # Проверьте, что пользователь вышел из аккаунта
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()
