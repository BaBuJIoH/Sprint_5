import pytest
from locators import Locators


def test_constructor_tabs(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    driver.find_element(*Locators.BUNS_SECTION).click()
    assert driver.find_element(*Locators.BUNS_SECTION).is_displayed()

    driver.find_element(*Locators.SAUCES_SECTION).click()
    assert driver.find_element(*Locators.SAUCES_SECTION).is_displayed()

    driver.find_element(*Locators.FILLINGS_SECTION).click()
    assert driver.find_element(*Locators.FILLINGS_SECTION).is_displayed()
    driver.quit()
