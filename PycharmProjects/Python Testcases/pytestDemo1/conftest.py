import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browserInstance():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    yield driver