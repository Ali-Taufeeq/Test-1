import pytest
from selenium import webdriver

@pytest.fixture(scope = "class")
def browserInstance():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver

