import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_constructor_tabs(driver):
    driver.get(Locators.BASE_URL)

    # Переход в конструктор
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()

    # Переход в раздел "Булки"
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUNS_SECTION)).click()
    assert driver.find_element(*Locators.BUNS_SECTION).is_displayed()

    # Переход в раздел "Соусы"
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SAUCES_SECTION)).click()
    assert driver.find_element(*Locators.SAUCES_SECTION).is_displayed()

    # Переход в раздел "Начинки"
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FILLINGS_SECTION)).click()
    assert driver.find_element(*Locators.FILLINGS_SECTION).is_displayed()
