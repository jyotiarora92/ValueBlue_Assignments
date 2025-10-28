import pytest
from selenium import webdriver
@pytest.fixture
def browser():
    #to initialize and cleanup selenium webdriver instance after test run
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()