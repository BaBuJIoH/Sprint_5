import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_buttons(driver):
    driver.get(Locators.BASE_URL)

    # Вход по кнопке «Войти в аккаунт» на главной
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)).click()

    # Ожидание и проверка перехода на страницу после логина
    WebDriverWait(driver, 5).until(EC.url_to_be(Locators.LOGIN_URL))
    assert driver.current_url == Locators.LOGIN_URL

    # Вход через кнопку «Личный кабинет»
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PERSONAL)).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Locators.LOGIN_URL))
    assert driver.current_url == Locators.LOGIN_URL

    # Вход через кнопку на странице логина
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Locators.LOGIN_URL))
    assert driver.current_url == Locators.LOGIN_URL
