import pytest
from selenium import webdriver

@pytest.fixture  # Фикстура инициализации браузера
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
