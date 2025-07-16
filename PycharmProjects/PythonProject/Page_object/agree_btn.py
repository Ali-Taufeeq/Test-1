from selenium import webdriver
from selenium.webdriver.common.by import By

from E2E_framework import driver


class Agree:
    def __init__(self,driver):
        self.driver = driver
        self.agree_btn = (By.XPATH,"//input[@id='termsofservice']")

    def agree(self):
        self.driver.find_element(*self.agree_btn).click()
